import os

from backend.app.services.parser_service import ParserService
from backend.app.services.chunking_service import ChunkingService
from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.vector_store_service import VectorStoreService


class PreloadService:

    def preload_documents(self):

        vector_store_service = VectorStoreService()

        # avoid re-indexing every restart
        if vector_store_service.collection.count() > 0:
            return

        parser_service = ParserService()
        chunking_service = ChunkingService()
        embedding_service = EmbeddingService()

        for filename in os.listdir("sample_documents"):

            file_path = os.path.join(
                "sample_documents",
                filename
            )

            pages = parser_service.extract_pages(file_path)

            chunks = chunking_service.chunk_pages(pages)

            embeddings = (
                embedding_service
                .generate_embeddings(chunks)
            )

            vector_store_service.add_chunks(
                chunks,
                embeddings
            )