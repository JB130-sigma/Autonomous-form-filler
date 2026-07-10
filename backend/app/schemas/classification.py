from pydantic import BaseModel, Field


class ClassificationResponse(BaseModel):
    """
    Response returned by the Document Classification Agent.
    """

    document_id: int

    document_type: str

    document_category: str

    confidence: float

    is_form: bool
    
    required_documents: list[str] = Field(default_factory=list)

    reason: str