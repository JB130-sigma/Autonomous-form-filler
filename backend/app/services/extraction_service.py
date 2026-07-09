from app.ocr.easyocr_engine import EasyOCREngine
from app.repositories.extracted_data_repository import (
    ExtractedDataRepository,
)
from app.repositories.document_repository import DocumentRepository


class ExtractionService:
    """
    Handles OCR extraction workflow.
    """

    def __init__(self, db):
        self.document_repository = DocumentRepository(db)
        self.extracted_repository = ExtractedDataRepository(db)
        self.ocr_engine = EasyOCREngine()

    def extract_document(self, document_id: int):
        """
        Extract text from a document.
        """

        document = self.document_repository.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found.")

        extracted_text = self.ocr_engine.extract_text(
            document.file_path
        )

        extracted_data = self.extracted_repository.create(
            document_id=document.id,
            extracted_text=extracted_text,
        )

        return extracted_data