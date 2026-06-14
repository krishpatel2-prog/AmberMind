from sentence_transformers import SentenceTransformer

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "paraphrase-MiniLM-L3-v2"
)

class EmbeddingService:

    def generate_embedding(
            self,
            text: str
    ):

        return self.model.encode(text)

    def generate_embeddings(
            self,
            chunks
    ):

        texts = []

        for chunk in chunks:

            texts.append(
                chunk["content"]
            )

        return self.model.encode(texts)