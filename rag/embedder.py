from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("BAAI/bge-m3")

    def encode(self, texts):
        return self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            normalize_embeddings=True
        )