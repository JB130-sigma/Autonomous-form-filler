from enum import Enum


class DocumentType(str, Enum):
    UNKNOWN = "unknown"

    # Identity Documents
    AADHAAR = "aadhaar"
    PAN = "pan"
    PASSPORT = "passport"
    DRIVING_LICENSE = "driving_license"
    VOTER_ID = "voter_id"

    # Forms
    BLANK_FORM = "blank_form"
    ONLINE_FORM = "online_form"

    # Other
    PHOTO = "photo"
    CERTIFICATE = "certificate"