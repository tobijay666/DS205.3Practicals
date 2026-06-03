from pypdf import PdfReader

class PDFProcessor:
    @staticmethod
    def extract_and_chunk(pdf_path: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() + "\n"
        
        # Chunking Logic
        chunks = []
        start = 0
        while start < len(full_text):
            end = start + chunk_size
            chunks.append(full_text[start:end])
            start += (chunk_size - overlap) # Move forward but keep some overlap
            
        return chunks