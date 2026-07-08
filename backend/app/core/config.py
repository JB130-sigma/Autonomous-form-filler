from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    """
    Application Configuration
    Reads values automatically from .env
    """

    # ==========================
    # Project
    # ==========================
    PROJECT_NAME: str
    PROJECT_VERSION: str
    DEBUG: bool

    # ==========================
    # Database
    # ==========================
    DATABASE_URL: str

    # ==========================
    # JWT Authentication
    # ==========================
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ==========================
    # Storage
    # ==========================
    UPLOAD_DIR: str
    MAX_FILE_SIZE_MB: int

    # ==========================
    # OCR
    # ==========================
    OCR_LANGUAGE: str

    # ==========================
    # Embedding Model
    # ==========================
    EMBEDDING_MODEL: str

    # ==========================
    # Vector Database
    # ==========================
    FAISS_INDEX_PATH: str

    # ==========================
    # Playwright
    # ==========================
    HEADLESS: bool

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


settings = Settings()