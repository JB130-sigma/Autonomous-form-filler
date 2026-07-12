import base64
from pathlib import Path


def encode_file_to_base64(file_path: str) -> str:
    """
    Convert a file into a Base64 string.
    """

    path = Path(file_path)

    with open(path, "rb") as file:
        encoded = base64.b64encode(file.read())

    return encoded.decode("utf-8")