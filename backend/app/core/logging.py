from loguru import logger
import sys

# Remove default logger
logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>",
    level="INFO",
)

# File Logger
logger.add(
    "logs/application.log",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
)

__all__ = ["logger"]