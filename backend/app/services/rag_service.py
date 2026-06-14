from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.vector_store_service import VectorStoreService
from backend.app.services.llm_services import LLMService
from backend.app.services.query_rewriter_service import QueryRewriterService
from backend.app.services.chat_history_service import ChatHistoryService

class RAGService:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store_service = VectorStoreService()

        self.llm_service = LLMService()

        self.chat_history_service = ChatHistoryService()

        self.query_rewriter_service = QueryRewriterService()

    def answer_question(self, question : str):

        standalone_question = (
            self.query_rewriter_service
            .rewrite_query(question)
        )

        #helps to add into history
        self.chat_history_service.add_message(
            "user",
            question
        )

        query_embedding = (
            self.embedding_service
            .generate_embedding(standalone_question)
        )

        results = (
            self.vector_store_service
            .retrieve(query_embedding)
        )

        print(results)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        #to remove the duplicate page source
        unique_sources = []
        seen = set()

        for metadata in metadatas:

            source_key = (
                metadata["source"],
                metadata["page"]
            )

            if source_key not in seen:
                seen.add(source_key)

                unique_sources.append(
                    {
                        "source" : metadata["source"],
                        "page" : metadata["page"]
                    }
                )


        context = "\n\n".join(documents)

        prompt = f"""
        You are a helpful AI assistant.

       Use the uploaded documents as your primary source.

        If the answer is present in the documents, answer using the document content.

        If the answer is not found, clearly indicate that the information was not found in the uploaded documents and then optionally provide a general answer from your own knowledge.

        Context:

        {context}

        Question:

        {standalone_question}
        """
        #ask groq
        answer = (
            self.llm_service
            .generate_response(prompt)
        )

         # adds the answer provided by llm into history
        self.chat_history_service.add_message(
            "assistant",
            answer
        )

        return {
        "answer" :answer,
        "sources" : unique_sources
        }