from sqlalchemy.orm import sessionmaker

from app.db.database import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency that provides a database session
    and automatically closes it after the request.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()