import argparse
import os
import time

from src.layout import detect_layout, visualize_layout
from src.chemistry import process_chemical_block
from src.ocr import init_vlm, extract_all_regions
from src.polish import init_polisher, polish_markdown
from src.export import save_markdown, compile_to_pdf


DEFAULT_IMAGE = "Example Lab Notebook Page.jpg"
DEFAULT_VLM_MODEL = "qwen3-vl:2b"
DEFAULT_POLISHER_MODEL = "qwen3.5:4b"


def parse_args():
    parser = argparse.ArgumentParser(description="Lab notebook OCR pipeline (Surya + local VLM)")
    parser.add_argument("image", nargs="?", default=DEFAULT_IMAGE, help="Path to lab notebook image")
    parser.add_argument("--vlm-model", default=DEFAULT_VLM_MODEL, help="Ollama vision model")
    parser.add_argument("--polish-model", default=DEFAULT_POLISHER_MODEL, help="Ollama text model for polish step")
    parser.add_argument("--output-md", default="polished_lab_notebook.md", help="Output markdown path")
    parser.add_argument("--output-pdf", default="final_lab_report.pdf", help="Output PDF path")
    parser.add_argument("--annotated-image", default=None, help="Save annotated layout image to this path")
    parser.add_argument("--skip-polish", action="store_true", help="Skip LLM polish step")
    parser.add_argument("--skip-pdf", action="store_true", help="Skip PDF compilation")
    return parser.parse_args()


def _elapsed(t0: float) -> str:
    return f"{time.perf_counter() - t0:.2f}s"


def main():
    args = parse_args()
    pipeline_start = time.perf_counter()

    if not os.path.exists(args.image):
        raise FileNotFoundError(f"Image not found: {args.image}")

    # 1. Layout detection
    print(f"\n[1/5] Detecting layout regions in '{args.image}'...")
    t0 = time.perf_counter()
    image, page_layout = detect_layout(args.image)
    print(f"  Layout detection done ({_elapsed(t0)})")

    if args.annotated_image:
        visualize_layout(image, page_layout, output_path=args.annotated_image)

    # 2. Init VLM
    print(f"\n[2/5] Initializing VLM '{args.vlm_model}'...")
    t0 = time.perf_counter()
    vlm = init_vlm(args.vlm_model)
    print(f"  VLM ready ({_elapsed(t0)})")

    # 3. Process chemical blocks first (dedicated prompt)
    print("\n[3/5] Processing chemical blocks...")
    chem_output = None
    for block in page_layout.bboxes:
        if block.label == "ChemicalBlock":
            print(f"  Found ChemicalBlock at {block.bbox}")
            t0 = time.perf_counter()
            chem_output = process_chemical_block(args.image, block.bbox, vlm)
            print(f"  Chemical block done ({_elapsed(t0)})")
            break  # notebook only processed the first one; extend here if needed

    # 4. Extract all regions
    print("\n[4/5] Extracting all layout regions...")
    t0 = time.perf_counter()
    parts = extract_all_regions(
        args.image,
        page_layout,
        vlm,
        chemical_block_output=chem_output,
    )
    raw_markdown = "".join(parts)
    print(f"  Region extraction done ({_elapsed(t0)})")

    # 5. Polish + export
    print("\n[5/5] Polishing and exporting...")
    if args.skip_polish:
        final_markdown = raw_markdown
    else:
        polisher = init_polisher(args.polish_model)
        t0 = time.perf_counter()
        final_markdown = polish_markdown(raw_markdown, polisher)
        print(f"  Polish done ({_elapsed(t0)})")

    save_markdown(final_markdown, args.output_md)

    if not args.skip_pdf:
        t0 = time.perf_counter()
        compile_to_pdf(final_markdown, args.output_pdf)
        print(f"  PDF compiled ({_elapsed(t0)})")

    print(f"\nDone. Total: {_elapsed(pipeline_start)}")


if __name__ == "__main__":
    main()
