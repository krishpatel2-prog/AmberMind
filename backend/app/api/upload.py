from fastapi import APIRouter
from fastapi import UploadFile, HTTPException
import os

from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.parser_service import ParserService
from backend.app.services.chunking_service import ChunkingService
from backend.app.services.vector_store_service import VectorStoreService

router = APIRouter()


@router.post("/upload")
def upload_pdf(
        file: UploadFile
):

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
            file_path,
            "wb"
    ) as pdf:

        pdf.write(
            file.file.read()
        )

    parser_service = ParserService()

    pages = (
        parser_service
        .extract_pages(file_path)
    )

    chunking_service = ChunkingService()

    chunks = (
        chunking_service
        .chunk_pages(pages)
    )

    embedding_service = EmbeddingService()

    embeddings = (
        embedding_service
        .generate_embeddings(chunks)
    )

    vector_store_service = VectorStoreService()

    vector_store_service.add_chunks(
        chunks,
        embeddings
    )

    return {
        "message": "PDF processed successfully"
    }


@router.delete("/upload")
def delete_upload(filename: str):
    # Prevent path traversal
    if os.path.basename(filename) != filename:
        raise HTTPException(status_code=400, detail="Invalid filename")

    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        os.remove(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "File deleted"}