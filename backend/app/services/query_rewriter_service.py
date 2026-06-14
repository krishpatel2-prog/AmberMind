from backend.app.services.llm_services import LLMService
from backend.app.services.chat_history_service import ChatHistoryService

class QueryRewriterService:

    def __init__(self):
        self.llm_service = LLMService()
        self.chat_history_service = ChatHistoryService()

    def rewrite_query(self, question: str):

        history = (
            self.chat_history_service.get_history()
        )

        prompt = f"""
        Given the conversation history and the latest question,
        rewrite the latest question into a standalone question.

        History:

        {history}

        Question:

        {question}

        Standalone Question:
        """
        standalone_question = (
            self.llm_service.generate_response(prompt)
        )

        return standalone_question