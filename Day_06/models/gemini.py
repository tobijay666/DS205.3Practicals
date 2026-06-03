import google.generativeai as genai
import os
from core.interfaces import LLMGenerator

class GeminiRAG(LLMGenerator):
    def __init__(self):
        genai.configure(api_key=os.getenv("GOOGLE_KEY"))
        self._model = genai.GenerativeModel('gemini-2.5-flash')

    def generate(self, prompt: str, context: str) -> str:
        augmented_prompt = f"""
        Use the following Context to answer the Question. 
        If the answer isn't in the context, say you don't know.
        
        CONTEXT: {context}
        QUESTION: {prompt}
        """
        response = self._model.generate_content(augmented_prompt)
        return response.text