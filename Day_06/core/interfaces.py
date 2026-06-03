from abc import ABC, abstractmethod

class LLMGenerator(ABC):
    @abstractmethod
    def generate(self, prompt: str, context: str) -> str:
        pass

class VectorDatabase(ABC):
    @abstractmethod
    def add_documents(self, texts: list[str]):
        pass

    @abstractmethod
    # Updated to take 'documents' AND 'ids'
    def add_pdfs(self, documents: list[str], ids: list[str]): 
        pass
    
    @abstractmethod
    def query(self, text: str, k: int = 3) -> list[str]:
        pass