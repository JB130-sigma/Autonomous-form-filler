from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from sqlalchemy import Enum
from app.enums import ProcessingStatus
from app.enums import DocumentType
from sqlalchemy import Float
from sqlalchemy import Boolean

class Document(Base):
    """
    Stores metadata for every uploaded document.
    The actual file is stored on disk, while this table
    keeps information about that file.
    """

    __tablename__ = "documents"
    
    is_form: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    original_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    stored_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )
    classification_confidence: Mapped[float] = mapped_column(
        Float,
        default=0.0,
        nullable=False
    )

    mime_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    file_size: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    #upload_status: Mapped[str] = mapped_column(
    #    String(50),
    #    default="uploaded"
    #)
    processing_status: Mapped[ProcessingStatus] = mapped_column(
        Enum(ProcessingStatus),
        default=ProcessingStatus.UPLOADED,
        nullable=False
    )
    document_type: Mapped[DocumentType] = mapped_column(
        Enum(DocumentType),
        default=DocumentType.UNKNOWN,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )