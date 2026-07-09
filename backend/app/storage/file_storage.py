import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile


class FileStorage:
    """
    Handles saving uploaded files to disk.
    """

    BASE_UPLOAD_DIR = Path("uploads")

    @classmethod
    def save_file(
        cls,
        user_id: int,
        file: UploadFile,
    ) -> tuple[str, str]:
        """
        Saves an uploaded file.

        Returns:
            stored_filename,
            file_path
        """

        # Create user directory
        user_folder = cls.BASE_UPLOAD_DIR / f"user_{user_id}"
        user_folder.mkdir(parents=True, exist_ok=True)

        # Preserve file extension
        extension = Path(file.filename).suffix

        # Generate unique filename
        stored_filename = f"{uuid.uuid4()}{extension}"

        # Full path
        file_path = user_folder / stored_filename

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return stored_filename, str(file_path)