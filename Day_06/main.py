from dotenv import load_dotenv
from db.vector_store import ChromaManager
from models.gemini import GeminiRAG
from pypdf import PdfReader
import os

class RAGSystem:
    def __init__(self, extractor, generator):
        self.db = extractor
        self.llm = generator

    def ingest_pdf(self, file_path: str):
        print(f"[*] Extracting text from {file_path}...")
        reader = PdfReader(file_path)
        chunks = [page.extract_text() for page in reader.pages if page.extract_text()]
    
        # Generate unique IDs
        file_name = os.path.basename(file_path)
            
        # Generating IDs for ChromaDB
        ids = [f"{file_name}_{i}" for i in range(len(chunks))]
        self.db.add_pdfs(chunks, ids)
        print(f"[+] Successfully indexed {len(chunks)} pages/chunks.")

    def ask(self, question: str):
        # 1. Retrieve
        context_chunks = self.db.query(question)
        context_str = " ".join(context_chunks)
        
        # 2. Generate
        return self.llm.generate(question, context_str)

if __name__ == "__main__":
    load_dotenv()

    app = RAGSystem(extractor=ChromaManager(), generator=GeminiRAG())
    
    # SETUP I 
    # Feeding a PDF
    app.ingest_pdf("Lecs\Slide 05 - RAG I.pdf")
    
    response = app.ask("What are the core drawbacks mentioned in the lecture?")
    print(f"Final Output: {response}")
    
    # Setup II
    # my_db = ChromaManager()
    # # Add some knowledge
    # my_db.add_documents(["The capital of France is Paris.", "The professor's name is Anton."])
    
    # # Run
    # rag_app = RAGSystem(extractor=my_db, generator=GeminiRAG())
    # print(rag_app.ask("Who is the professor?"))