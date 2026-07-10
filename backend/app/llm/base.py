from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLM providers.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
        file_path: str | None = None,
        response_format: str = "text",
        temperature: float = 0,
        max_tokens: int = 100,
    ) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt: Instruction sent to the model.
            file_path: Optional path to an image or PDF.

        Returns:
            Model response as a string.
        """
        pass