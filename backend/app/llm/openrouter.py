import mimetypes

from openai import OpenAI

from app.core.config import settings
from app.llm.base import BaseLLM
from app.utils.file_encoder import encode_file_to_base64

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
        Generate a response using OpenRouter.
        Supports text-only and image inputs.
        """

        # Default: text-only message
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        # If an image is provided, send it as multimodal input
        if file_path:

            mime_type, _ = mimetypes.guess_type(file_path)

            if mime_type and mime_type.startswith("image/"):

                image_base64 = encode_file_to_base64(file_path)

                messages = [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt,
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{mime_type};base64,{image_base64}"
                                },
                            },
                        ],
                    }
                ]

        response = self.client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content