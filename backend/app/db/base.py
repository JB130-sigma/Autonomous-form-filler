from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database models.
    Every SQLAlchemy model will inherit from this class.
    """
    pass