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

    PASSPORT_APPLICATION = "passport_application"
    BANK_ACCOUNT_OPENING_FORM = "bank_account_opening_form"
    DRIVING_LICENSE_APPLICATION = "driving_license_application"
    COLLEGE_ADMISSION_FORM = "college_admission_form"
    SCHOLARSHIP_FORM = "scholarship_form"
    INCOME_CERTIFICATE_FORM = "income_certificate_form"

    # Supporting Documents
    PHOTO = "photo"
    SIGNATURE = "signature"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    CERTIFICATE = "certificate"