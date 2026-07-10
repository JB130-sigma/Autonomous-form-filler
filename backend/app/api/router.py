from fastapi import APIRouter

from app.api.application import router as application_router
from app.api.auth import router as auth_router
from app.api.extraction import router as extraction_router
from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.classification import router as classification_router
router = APIRouter()

# Health APIs
router.include_router(health_router)

# Authentication APIs
router.include_router(auth_router)

# Application APIs
router.include_router(application_router)

# Upload APIs
router.include_router(upload_router)

# OCR / Extraction APIs
router.include_router(extraction_router)

# Classification APIs
router.include_router(classification_router)