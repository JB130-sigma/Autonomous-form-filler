from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document_repository import DocumentRepository
from app.storage.file_storage import FileStorage
from app.enums import DocumentType, ProcessingStatus

class UploadService:
    """
    Handles document upload workflow.
    """

    def __init__(self, db: Session):
        self.repository = DocumentRepository(db)

    def upload_document(
        self,
        user_id: int,
        file: UploadFile,
    ) -> Document:
        """
        Save uploaded file and create database record.
        """

        # Save file to disk
        stored_filename, file_path = FileStorage.save_file(
            user_id=user_id,
            file=file,
        )

        # Create database model
        document = Document(
            user_id=user_id,
            original_filename=file.filename,
            stored_filename=stored_filename,
            file_path=file_path,
            mime_type=file.content_type,
            file_size=file.size if file.size else 0,

            document_type=DocumentType.UNKNOWN,
            processing_status=ProcessingStatus.UPLOADED,
            classification_confidence=0.0,
            is_form=False,
)

        # Save metadata
        return self.repository.create(document)