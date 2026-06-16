import base64
from io import BytesIO
from PIL import Image
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama


def init_vlm(model: str = "qwen3-vl:2b") -> ChatOllama:
    return ChatOllama(model=model, reasoning=False)


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
    document_parts: list[str] = []

    print(f"Processing {total} layout regions...\n")

    for i, block in enumerate(sorted_blocks):
        label = block.label
        bbox = block.bbox

        if label in skip_labels:
            continue

        if label == "ChemicalBlock":
            print(f"[{i+1}/{total}] ChemicalBlock — using pre-processed output.")
            if chemical_block_output:
                document_parts.append(f"\n{chemical_block_output}\n")
            continue

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

        try:
            print(f"[{i+1}/{total}] Extracting {label} at {bbox}...")
            response = vlm.invoke([message])
            content = response.content.strip()
            document_parts.append(format_content(label, content))
        except Exception as e:
            print(f"  Warning: failed on region {i+1}: {e}")

    return document_parts
