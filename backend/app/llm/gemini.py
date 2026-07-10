from app.llm.base import BaseLLM


class GeminiClient(BaseLLM):
    """
    Gemini LLM provider.
    """

    def generate(
        self,
        prompt: str,
        file_path: str | None = None,
        response_format: str = "text",
        temperature: float = 0,
        max_tokens: int = 100,
    ) -> str:
        """
        Generate a response using Gemini.
        """

        raise NotImplementedError(
            "Gemini provider is not implemented yet."
        )