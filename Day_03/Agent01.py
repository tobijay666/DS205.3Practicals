import os
import google.generativeai as genai
from dotenv import load_dotenv
from abc import ABC, abstractmethod

# 1. Load the secrets from .env


class LLMModel(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class GeminiWrapper(LLMModel):
    def __init__(self):
        genai.configure(api_key=os.environ['GOOGLE_KEY'])
        self._model = genai.GenerativeModel(_____?)#LLModel

    def generate(self, prompt: str) -> str:
        response = self._model.generate_content(prompt)
        return response.text


class InferenceAgent:
    def __init__(self, model: LLMModel):
        # Dependency Injection

    def run(self, query: str):
        print(f"Agent processing: {query}")
        return self._model.generate(query)

if __name__ == "__main__":
    # Assemble the system
    
    result = agent.run("why is the sky blue in one sentence?")
    print(f"Response: {result}")