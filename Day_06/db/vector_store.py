from core.interfaces import VectorDatabase 
import chromadb
from chromadb.utils import embedding_functions

class ChromaManager(VectorDatabase):
    def __init__(self, collection_name="class_notes"):
        # Using a standard sentence-transformer as the unified "Tokenizer"
        self._embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self._client = chromadb.PersistentClient(path="./chroma_db")
        self._collection = self._client.get_or_create_collection(
            name=collection_name, 
            embedding_function=self._embed_fn
        )

    def add_documents(self, texts: list[str]):
        ids = [f"id_{i}" for i in range(len(texts))]
        self._collection.add(documents=texts, ids=ids)

    def add_pdfs(self, documents: list[str], ids: list[str]):
        self._collection.add(
            documents=documents, 
            ids=ids
        )


    def query(self, text: str, k: int = 2) -> list[str]:
        results = self._collection.query(query_texts=[text], n_results=k)
        return results['documents'][0]