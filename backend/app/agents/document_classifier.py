import json

from app.llm.factory import LLMFactory
from app.prompts.document_classifier_prompt import DOCUMENT_CLASSIFIER_PROMPT
from app.schemas.classification import ClassificationResponse


class DocumentClassifier:
    """
    AI Agent responsible for classifying uploaded documents.
    """

    def __init__(self):
        self.llm = LLMFactory.create()

    def classify(
        self,
        document_id: int,
        file_path: str,
    ) -> ClassificationResponse:
        """
            Classify the uploaded document using the LLM.
        """

        response = self.llm.generate(
            prompt=DOCUMENT_CLASSIFIER_PROMPT,
            file_path=file_path,
            response_format="json",
            temperature=0,
            max_tokens=200,
        )

        print("\n========== LLM RESPONSE ==========")
        print(response)
        print("==================================\n")

        response = response.strip()
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:
            data = json.loads(response)
        except json.JSONDecodeError:
            raise ValueError(
                f"LLM returned invalid JSON:\n{response}"
        )

        return ClassificationResponse(
            document_id=document_id,
            **data
        )