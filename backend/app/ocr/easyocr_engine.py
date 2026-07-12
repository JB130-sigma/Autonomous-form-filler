import fitz  # PyMuPDF
import easyocr
import numpy as np

from PIL import Image

from app.ocr.ocr_engine import OCREngine


class EasyOCREngine(OCREngine):
    """
    OCR implementation using EasyOCR.
    """

    def __init__(self):
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

        try:
            # Load image using Pillow
            image = Image.open(image_path).convert("RGB")

            # Convert to NumPy array
            image_np = np.array(image)

            # OCR
            results = self.reader.readtext(
                image_np,
                detail=0
            )

            return "\n".join(results)

        except Exception as e:
            raise RuntimeError(
                f"EasyOCR failed for image '{image_path}': {e}"
            )

    def _extract_from_pdf(self, pdf_path: str) -> str:
        """
        OCR for PDF files.
        """

        text = ""

        pdf = fitz.open(pdf_path)

        for page_number, page in enumerate(pdf):

            pix = page.get_pixmap(dpi=300)

            temp_image = f"temp_page_{page_number}.png"

            pix.save(temp_image)

            page_text = self._extract_from_image(temp_image)

            text += page_text + "\n"

        pdf.close()

        return text