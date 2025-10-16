from .agents.writer_agent import write_text
from .agents.reviewer_agent import review_text
from .agents.translator_agent import translate_to_english


def run_autogen_team(task: str) -> str:
    """Simulate a conversation between writer -> reviewer -> translator"""
    writer_output = write_text(task)
    reviewer_output = review_text(writer_output)
    translator_output = translate_to_english(reviewer_output)
    return "\n".join([writer_output, reviewer_output, translator_output])
