from enum import Enum


class ApplicationStatus(str, Enum):
    CREATED = "created"

    WAITING_FOR_DOCUMENTS = "waiting_for_documents"

    PROCESSING = "processing"

    READY_FOR_REVIEW = "ready_for_review"

    COMPLETED = "completed"

    FAILED = "failed"