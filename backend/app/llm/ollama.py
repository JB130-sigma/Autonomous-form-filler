from app.llm.base import BaseLLM


class OllamaClient(BaseLLM):
    """
    Ollama LLM provider.
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
        Generate a response using Ollama.
        """

        raise NotImplementedError(
            "Ollama provider is not implemented yet."
        )