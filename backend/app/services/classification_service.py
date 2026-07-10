from app.agents.document_classifier import DocumentClassifier
from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.enums.processing_status import ProcessingStatus
from app.schemas import document
from sqlalchemy.orm import Session


class ClassificationService:
    """
    Handles document classification workflow.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = DocumentRepository(db)
        self.classifier = DocumentClassifier()

    def classify_document(self, document_id: int):

        document = self.repository.get_by_id(document_id)

        if document is None:
            raise ValueError("Document not found.")

        result = self.classifier.classify(
            document_id=document.id,
            file_path=document.file_path,
        )

        document.document_type = result.document_type
        document.document_category = result.document_category
        document.processing_status = ProcessingStatus.CLASSIFIED

        self.db.commit()
        self.db.refresh(document)

        return result