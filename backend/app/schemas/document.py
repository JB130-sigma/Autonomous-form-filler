from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    """
    Response returned after a successful upload.
    """

    id: int
    original_filename: str
    mime_type: str
    file_size: int
    document_type: str
    processing_status: str
    classification_confidence: float
    is_form: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class DocumentListResponse(BaseModel):
    """
    Response used when listing user documents.
    """

    id: int
    original_filename: str
    mime_type: str
    file_size: int
    upload_status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)