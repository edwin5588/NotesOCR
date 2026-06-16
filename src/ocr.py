import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from PIL import Image
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


PARALLEL_WORKERS = 4


def init_vlm(model: str = "qwen3-vl:2b") -> ChatOllama:
    return ChatOllama(model=model)


def get_prompt(label: str) -> str:
    if label == "Equation":
        return (
            "You are an expert mathematical transcriber. Convert this handwritten formula or derivation "
            "into a single clean line of raw LaTeX string. Do not wrap it in markdown block tokens or add conversational text."
        )
    if label == "Table":
        return (
            "You are an expert data parser. Convert this handwritten data grid into a clean, "
            "standard Markdown table syntax. Ensure column boundaries and headers line up correctly."
        )
    if label == "SectionHeader":
        return "Transcribe this section header title text exactly as written. Output only the plain text string."
    return (
        "Transcribe this handwritten laboratory text block exactly as written. "
        "Carefully preserve all scientific units (e.g., °C, mol%, A, s), variables, and abbreviations."
    )


def format_content(label: str, content: str) -> str:
    if label == "SectionHeader":
        return f"\n## {content}\n"
    if label == "Equation":
        return f"\n$$\n{content}\n$$\n"
    return f"\n{content}\n"


def _extract_region(args):
    i, total, img_path, label, bbox, vlm = args

    with Image.open(img_path).convert("RGB") as img:
        crop = img.crop([int(c) for c in bbox])

    buffered = BytesIO()
    crop.save(buffered, format="JPEG")
    b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

    message = HumanMessage(
        content=[
            {"type": "text", "text": get_prompt(label)},
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{b64}"},
        ]
    )

    print(f"[{i+1}/{total}] Extracting {label} at {bbox}...")
    response = vlm.invoke([message])
    return format_content(label, response.content.strip())


def extract_all_regions(
    img_path: str,
    page_layout,
    vlm,
    skip_labels: set = None,
    chemical_block_output: str = None,
) -> list[str]:
    if skip_labels is None:
        skip_labels = {"PageHeader", "PageFooter"}

    sorted_blocks = sorted(page_layout.bboxes, key=lambda b: b.bbox[1])
    total = len(sorted_blocks)

    print(f"Processing {total} layout regions...\n")

    # Build work list, preserving index for ordering
    tasks = []
    placeholders = {}
    for i, block in enumerate(sorted_blocks):
        label, bbox = block.label, block.bbox
        if label in skip_labels:
            continue
        if label == "ChemicalBlock":
            print(f"[{i+1}/{total}] ChemicalBlock — using pre-processed output.")
            if chemical_block_output:
                placeholders[i] = f"\n{chemical_block_output}\n"
            continue
        tasks.append((i, total, img_path, label, bbox, vlm))

    results = {}
    with ThreadPoolExecutor(max_workers=PARALLEL_WORKERS) as executor:
        future_to_idx = {executor.submit(_extract_region, t): t[0] for t in tasks}
        for future in as_completed(future_to_idx):
            i = future_to_idx[future]
            try:
                results[i] = future.result()
            except Exception as e:
                print(f"  Warning: failed on region {i+1}: {e}")

    results.update(placeholders)
    return [results[i] for i in sorted(results)]
