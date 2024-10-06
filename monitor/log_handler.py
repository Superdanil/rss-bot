import sys

from loguru import logger

from settings import settings

logger.add(
    settings.MONITOR_LOGFILE,
    rotation=settings.ROTATION,
    compression=settings.COMPRESSION,
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="INFO"
)

logger.add(sys.stderr, level="DEBUG")
