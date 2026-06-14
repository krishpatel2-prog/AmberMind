from fastapi import APIRouter

from backend.app.services.rag_service import RAGService
from backend.app.models.chat_models import ChatRequest, ChatResponse

router = APIRouter()

rag_service = RAGService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(
        request: ChatRequest
):

    result = (
        rag_service
        .answer_question(
            request.message
        )
    )

    return ChatResponse(
        response=result["answer"],
        sources = result["sources"]
    )

