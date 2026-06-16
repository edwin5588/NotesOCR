from PIL import Image, ImageDraw
from surya.layout import LayoutPredictor

COLOR_MAP = {
    "Text": "blue",
    "Table": "green",
    "SectionHeader": "red",
    "Title": "purple",
    "Formula": "orange",
    "Equation": "orange",
    "Figure": "cyan",
    "Picture": "cyan",
    "ChemicalBlock": "darkgreen",
    "Diagram": "magenta",
    "ListGroup": "yellow",
}


def detect_layout(image_path: str):
    image = Image.open(image_path).convert("RGB")
    predictor = LayoutPredictor()
    predictions = predictor([image])
    page_layout = predictions[0]
    return image, page_layout


def visualize_layout(image: Image.Image, page_layout, output_path: str = None) -> Image.Image:
    annotated = image.copy()
    draw = ImageDraw.Draw(annotated)

    print("Detected regions:")
    for block in page_layout.bboxes:
        box = block.bbox
        label = block.label
        color = COLOR_MAP.get(label, "magenta")
        print(f"  - {label}: {box}")
        draw.rectangle(box, outline=color, width=3)
        draw.text((box[0] + 2, box[1] + 2), label, fill=color)

    if output_path:
        annotated.save(output_path)
        print(f"Saved annotated image to {output_path}")

    return annotated
