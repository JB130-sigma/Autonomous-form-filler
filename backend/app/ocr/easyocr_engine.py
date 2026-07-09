import fitz  # PyMuPDF
import easyocr

from app.ocr.ocr_engine import OCREngine


class EasyOCREngine(OCREngine):
    """
    OCR implementation using EasyOCR.
    """

    def __init__(self):
        # English for now.
        # Later we'll add multiple languages.
        self.reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    def extract_text(self, file_path: str) -> str:
        """
        Extract text from an image or PDF.
        """

        if file_path.lower().endswith(".pdf"):
            return self._extract_from_pdf(file_path)

        return self._extract_from_image(file_path)

    def _extract_from_image(self, image_path: str) -> str:
        """
        OCR for image files.
        """

        results = self.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(results)

    def _extract_from_pdf(self, pdf_path: str) -> str:
        """
        OCR for PDF files.
        """

        text = ""

        pdf = fitz.open(pdf_path)

        for page in pdf:

            pix = page.get_pixmap()

            temp_image = "temp_page.png"

            pix.save(temp_image)

            page_text = self._extract_from_image(
                temp_image
            )

            text += page_text + "\n"

        pdf.close()

        return text