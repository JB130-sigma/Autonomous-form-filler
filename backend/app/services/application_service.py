from sqlalchemy.orm import Session

from app.models.application import Application
from app.repositories.application_repository import ApplicationRepository
from app.schemas.application import ApplicationCreate


class ApplicationService:
    """
    Handles business logic related to applications.
    """

    def __init__(self, db: Session):
        self.repository = ApplicationRepository(db)

    def create_application(
        self,
        user_id: int,
        application_data: ApplicationCreate,
    ) -> Application:
        """
        Create a new application for a user.
        """

        application = Application(
            user_id=user_id,
            application_name=application_data.application_name,
            application_type=application_data.application_type,
        )

        return self.repository.create(application)

    def get_application(
        self,
        application_id: int,
    ):
        """
        Retrieve a single application by ID.
        """

        return self.repository.get_by_id(application_id)

    def get_user_applications(
        self,
        user_id: int,
    ):
        """
        Retrieve all applications belonging to a user.
        """

        return self.repository.get_by_user(user_id)

    def update_status(
        self,
        application: Application,
        status,
    ):
        """
        Update application status.
        """

        application.status = status
        return self.repository.update(application)

    def delete_application(
        self,
        application: Application,
    ):
        """
        Delete an application.
        """

        self.repository.delete(application)