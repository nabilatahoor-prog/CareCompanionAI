import streamlit as st
import google.generativeai as genai
from pathlib import Path

class GeminiChat:
    def __init__(self):
        self.model = None
        self.api_key = None
        self._setup()
    
    def _setup(self):
        api_key_file = Path(__file__).parent.parent.parent / 'secrets' / 'gemini_key.txt'
        if api_key_file.exists():
            with open(api_key_file, 'r') as f:
                self.api_key = f.read().strip()
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
    
    def get_response(self, prompt, context=""):
        if not self.model:
            return self._mock_response(prompt)
        
        try:
            full_prompt = f"Context: {context}\n\nUser: {prompt}\nAssistant:"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"AI Error: {e}"
    
    def _mock_response(self, prompt):
        responses = {
            "blood pressure": "Your blood pressure should be checked regularly. Normal range is 120/80.",
            "medication": "Always take medications as prescribed by your doctor.",
            "appointment": "I can help you schedule or find information about appointments.",
            "symptom": "Please consult your doctor for any concerning symptoms."
        }
        
        for key, response in responses.items():
            if key in prompt.lower():
                return response
        return "I'm your health assistant. How can I help you today?"

gemini_chat = GeminiChat()
