from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:
    """
    Handles all database operations related to documents.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, document: Document) -> Document:
        """
        Save a new document.
        """
        self.db.add(document)
        self.db.commit()
        self.db.refresh(document)
        return document

    def get_by_id(self, document_id: int) -> Document | None:
        """
        Get a document by its ID.
        """
        return (
            self.db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

    def get_by_user(self, user_id: int) -> list[Document]:
        """
        Get all documents uploaded by a user.
        """
        return (
            self.db.query(Document)
            .filter(Document.user_id == user_id)
            .all()
        )

    def update(self, document: Document) -> Document:
        """
        Update an existing document.
        """
        self.db.commit()
        self.db.refresh(document)
        return document

    def delete(self, document: Document) -> None:
        """
        Delete a document.
        """
        self.db.delete(document)
        self.db.commit()