from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.classification import ClassificationResponse
from app.services.classification_service import ClassificationService

router = APIRouter(
    prefix="/classification",
    tags=["Document Classification"],
)


@router.post(
    "/{document_id}",
    response_model=ClassificationResponse,
)
def classify_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    """
    Classify an uploaded document using the AI Classification Agent.
    """

    service = ClassificationService(db)

    try:
        return service.classify_document(document_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )