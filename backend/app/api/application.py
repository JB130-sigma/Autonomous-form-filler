from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse,
    ApplicationListResponse,
)
from app.services.application_service import ApplicationService

router = APIRouter(
    prefix="/applications",
    tags=["Applications"],
)


# Temporary user ID
# Later this will come from JWT authentication
CURRENT_USER_ID = 1


@router.post(
    "/",
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new application.
    """

    service = ApplicationService(db)

    return service.create_application(
        user_id=CURRENT_USER_ID,
        application_data=application_data,
    )


@router.get(
    "/",
    response_model=list[ApplicationListResponse],
)
def get_user_applications(
    db: Session = Depends(get_db),
):
    """
    Get all applications of the current user.
    """

    service = ApplicationService(db)

    return service.get_user_applications(CURRENT_USER_ID)


@router.get(
    "/{application_id}",
    response_model=ApplicationResponse,
)
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
):
    """
    Get one application by ID.
    """

    service = ApplicationService(db)

    application = service.get_application(application_id)

    if application is None:
        raise HTTPException(
            status_code=404,
            detail="Application not found.",
        )

    return application