from openai import OpenAI

from app.core.config import settings
from app.llm.base import BaseLLM


class OpenRouterClient(BaseLLM):
    """
    OpenRouter LLM provider.
    """

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(
        self,
        prompt: str,
        file_path: str | None = None,
        response_format: str = "text",
        temperature: float = 0,
        max_tokens: int = 100,
    ) -> str:
        """
        Generate a text response using OpenRouter.
        """

        response = self.client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content