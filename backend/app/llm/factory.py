from app.core.config import settings

from app.llm.gemini import GeminiClient
from app.llm.ollama import OllamaClient
from app.llm.openrouter import OpenRouterClient


class LLMFactory:
    """
    Factory responsible for returning the configured LLM provider.
    """

    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        if provider == "openrouter":
            return OpenRouterClient()

        elif provider == "gemini":
            return GeminiClient()

        elif provider == "ollama":
            return OllamaClient()

        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )