from abc import ABC, abstractmethod


class OCREngine(ABC):
    """
    Abstract base class for all OCR engines.
    """

    @abstractmethod
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from the given file.

        Args:
            file_path (str): Path to the document.

        Returns:
            str: Extracted text.
        """
        pass