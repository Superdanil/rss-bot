from loguru import logger

from core.settings import settings


def record_error_log(message):
    logger.add(
        sink=settings.ERRORLOGFILE,
        format="{time}|{message}\n",
        rotation=settings.ROTATION,
        compression=settings.COMPRESSION,
    )
    logger.error(message)

