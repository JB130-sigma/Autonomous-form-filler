from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.document import DocumentResponse
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/upload",
    tags=["Document Upload"],
)


@router.post(
    "/",
    response_model=DocumentResponse,
)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload a document.
    """

    # Temporary user id
    # Later we'll replace this with JWT authentication
    user_id = 1

    service = UploadService(db)

    return service.upload_document(
        user_id=user_id,
        file=file,
    )