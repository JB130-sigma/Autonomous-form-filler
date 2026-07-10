from enum import Enum


class ProcessingStatus(str, Enum):
    UPLOADED = "uploaded"

    CLASSIFIED = "classified"

    OCR_COMPLETED = "ocr_completed"

    PARSED = "parsed"

    PROFILE_CREATED = "profile_created"

    VALIDATED = "validated"

    FILLED = "filled"

    COMPLETED = "completed"

    FAILED = "failed"