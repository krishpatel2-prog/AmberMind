class ChatHistoryService:

    history = []

    def add_message(self, role, content):
        ChatHistoryService.history.append(
            {
                "role": role,
                "content": content
            }
        )

    def get_history(self):

        return ChatHistoryService.history