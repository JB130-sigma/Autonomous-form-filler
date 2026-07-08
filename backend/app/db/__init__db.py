from app.db.base import Base
from app.db.database import engine

# Import all models
from app.models.user import User


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)