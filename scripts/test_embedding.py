    import pandas as pd
from rag.embedder import Embedder

df = pd.read_json(
    "data/lex_uz_unified.jsonl",
    lines=True
)

embedder = Embedder()

embeddings = embedder.encode(
    df["content"].head(5).tolist()
)

print(embeddings.shape)
print(embeddings[0][:10])    