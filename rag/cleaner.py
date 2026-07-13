import re


def clean_text(text: str) -> str:
    """
    Clean legal text.
    """

    if text is None:
        return ""

    text = str(text)

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    text = re.sub(r"\s+", " ", text)

    return text.strip()