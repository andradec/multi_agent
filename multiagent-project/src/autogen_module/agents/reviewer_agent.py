
def review_text(text: str) -> str:
    # Simple reviewer stub that 'improves' text
    improved = text.replace('Generated', 'Refined')
    return f"[Reviewer] {improved}"
