from typing import List


def chunk_text(text: str,
               chunk_size: int = 1200,
               overlap: int = 200) -> List[str]:

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start = end - overlap

    return chunks