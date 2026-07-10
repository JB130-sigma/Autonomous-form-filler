from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ApplicationCreate(BaseModel):
    """
    Request schema for creating a new application.
    """

    application_name: str
    application_type: str


class ApplicationResponse(BaseModel):
    """
    Response schema returned after creating or retrieving an application.
    """

    id: int
    user_id: int
    application_name: str
    application_type: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ApplicationListResponse(BaseModel):
    """
    Response schema used when listing user applications.
    """

    id: int
    application_name: str
    application_type: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)