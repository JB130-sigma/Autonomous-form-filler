from datetime import datetime

from pydantic import BaseModel


class ExtractedDataResponse(BaseModel):
    """
    Response schema for OCR extracted data.
    """

    id: int
    document_id: int
    extracted_text: str
    created_at: datetime

    class Config:
        from_attributes = True