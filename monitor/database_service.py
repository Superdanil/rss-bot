import requests
from requests import RequestException

from dtos import NewsDTO, SourceDTO
from log_handler import logger
from settings import settings


class DatabaseService:
    """Класс работы с сервисом базы данных."""

    def __init__(self):
        self._database_url = settings.database_url

    def get_rss_sources(self) -> list[SourceDTO] | None:
        """Возвращает список rss-источников из сервиса базы данных"""
        try:
            response = requests.get(url=f"{self._database_url}/sources")
            return [SourceDTO(**source) for source in response.json()]

        except RequestException as e:
            logger.error(f"При получении списка RSS-источников возникло исключение: {e}")
            return None

    def add_news(self, news_list: list[NewsDTO]):
        """Отправляет новости в сервис базы данных."""
        news_list = [news.model_dump(mode="json") for news in news_list]
        try:
            response = requests.post(url=f"{self._database_url}/news", json=news_list)
            return response.json()

        except RequestException as e:
            logger.error(f"При добавлении новостей в базу данных возникло исключение: {e}")
            return []


database_service = DatabaseService()
