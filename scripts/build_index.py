import pandas as pd

from rag.cleaner import clean_text
from rag.chunker import chunk_text


print("Loading dataset...")

df = pd.read_json(
    "data/lex_uz_unified.jsonl",
    lines=True
)

print(df.head())

print()

print(df.shape)

print()

sample = clean_text(df.iloc[0]["content"])

chunks = chunk_text(sample)

print()

print("Chunks:", len(chunks))

print()

print(chunks[0])