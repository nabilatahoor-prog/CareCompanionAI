import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


class GeminiService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = None
        self._setup()

    def _setup(self):
        if not self.api_key:
            return

        try:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-pro")
        except Exception:
            self.model = None

    def is_available(self):
        return self.model is not None

    async def health_chat(self, user_id, message, context=""):
        if not self.is_available():
            return (
                "Gemini is not configured yet. "
                "Add GEMINI_API_KEY to your .env file to enable AI responses."
            )

        prompt = f"""
You are CareCompanionAI, a careful health companion for seniors.

Rules:
- Do not diagnose.
- Do not replace a doctor.
- Encourage emergency care for urgent symptoms.
- Keep responses short, clear, and reassuring.

User ID: {user_id}

Health context:
{context}

User message:
{message}
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini error: {e}"


gemini_service = GeminiService()