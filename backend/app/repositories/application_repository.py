from sqlalchemy.orm import Session

from app.models.application import Application


class ApplicationRepository:
    """
    Handles all database operations related to applications.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, application: Application) -> Application:
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application

    def get_by_id(self, application_id: int):
        return (
            self.db.query(Application)
            .filter(Application.id == application_id)
            .first()
        )

    def get_by_user(self, user_id: int):
        return (
            self.db.query(Application)
            .filter(Application.user_id == user_id)
            .all()
        )

    def update(self, application: Application) -> Application:
        self.db.commit()
        self.db.refresh(application)
        return application

    def delete(self, application: Application):
        self.db.delete(application)
        self.db.commit()