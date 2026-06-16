from langchain_ollama import OllamaLLM


def init_polisher(model: str = "qwen3.5:4b") -> OllamaLLM:
    return OllamaLLM(model=model, reasoning=False, temperature=0.2)


def polish_markdown(raw_markdown: str, polisher: OllamaLLM) -> str:
    prompt = f"""You are an expert technical editor. Your sole task is to take the raw, \
sequentially stitched lab notebook text provided below and give it a clean "global polish" for layout presentation.

Strict Rules:
1. Retain the text, data points, dates, and values EXACTLY word-for-word from the source. Do not alter, add, or drop any experimental values or names.
2. Clean up any loose formatting artifacts (such as broken markdown pipes in the table or missing delimiters).
3. Ensure all mathematical derivations are fully wrapped in clean inline LaTeX blocks ($inline$ or \\Latex[block]).
4. Infer and apply missing structural headers or clear spacing only where it enhances readability.
5. Create a final conclusion of experiment + findings.

Raw Source Document:
---
{raw_markdown}
---

Output only the polished, final Markdown text. Do not include any introductory remarks, explanations, or conversational filler."""

    print("Running polish step...")
    return polisher.invoke(prompt)
