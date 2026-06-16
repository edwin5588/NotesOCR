import pypandoc


def save_markdown(text: str, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Saved markdown to {path}")


def compile_to_pdf(md_text: str, output_filename: str = "final_lab_report.pdf") -> bool:
    print("Compiling to PDF...")
    extra_args = [
        "--pdf-engine=pdflatex",
        "-V", "geometry:margin=0.75in",
        "-V", "fontfamily=helvet",
    ]
    try:
        pypandoc.convert_text(
            md_text,
            to="pdf",
            format="md",
            outputfile=output_filename,
            extra_args=extra_args,
        )
        print(f"PDF saved to {output_filename}")
        return True
    except Exception as e:
        print(f"PDF compilation failed: {e}")
        return False
