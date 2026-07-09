from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.extracted_data import ExtractedDataResponse
from app.services.extraction_service import ExtractionService

router = APIRouter(
    prefix="/extract",
    tags=["OCR Extraction"],
)


@router.post(
    "/{document_id}",
    response_model=ExtractedDataResponse,
)
def extract_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    """
    Extract text from an uploaded document.
    """

    service = ExtractionService(db)

    try:
        return service.extract_document(document_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )