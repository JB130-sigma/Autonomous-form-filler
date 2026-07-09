from sqlalchemy.orm import Session

from app.models.extracted_data import ExtractedData


class ExtractedDataRepository:
    """
    Repository for OCR extracted data.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        document_id: int,
        extracted_text: str,
    ) -> ExtractedData:
        """
        Save OCR result.
        """

        extracted_data = ExtractedData(
            document_id=document_id,
            extracted_text=extracted_text,
        )

        self.db.add(extracted_data)
        self.db.commit()
        self.db.refresh(extracted_data)

        return extracted_data

    def get_by_document_id(
        self,
        document_id: int,
    ) -> ExtractedData | None:
        """
        Retrieve OCR result for a document.
        """

        return (
            self.db.query(ExtractedData)
            .filter(
                ExtractedData.document_id == document_id
            )
            .first()
        )