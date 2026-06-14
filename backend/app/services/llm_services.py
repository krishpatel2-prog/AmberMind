from groq import Groq
from backend.app.core.config import settings

class LLMService:

    def __init__(self):
        # Creates a connection to Groq.
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_response(self, message:str):

        response = self.client.chat.completions.create(
            model= settings.MODEL_NAME,
            messages=[{  #LLMs understand conversations as lists []
                "role" : "user",
                "content" : message
            }]
        )

        return response.choices[0].message.content


