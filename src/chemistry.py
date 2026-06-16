import base64
from io import BytesIO
from PIL import Image
from langchain_core.messages import HumanMessage


def encode_image_to_base64(pil_image: Image.Image) -> str:
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def process_chemical_block(img_path: str, bbox: list, vlm) -> str:
    with Image.open(img_path).convert("RGB") as img:
        crop = img.crop([int(c) for c in bbox])

    b64 = encode_image_to_base64(crop)
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": (
                    "Analyze this cropped section of a chemical lab notebook page. "
                    "Transcribe the chemical reaction equation. Convert any hand-drawn molecular "
                    "structures into valid SMILES strings or accurate chemical formulas, and "
                    "extract all written reaction conditions (voltages, reagents)."
                ),
            },
            {"type": "image_url", "image_url": f"data:image/jpeg;base64,{b64}"},
        ]
    )
    response = vlm.invoke([message])
    return response.content.strip()
