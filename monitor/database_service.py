import httpx

from monitor.settings import settings


class DatabaseService:
    """Класс работы с сервисом базы данных."""

    def __init__(self):
        self._database_url = settings.database_url

    def get_rss_sources(self) -> list[str]:
        """Возвращает список rss-источников из сервиса базы данных."""
        try:
            with httpx.Client() as client:
                response = client.get(url=f"{self._database_url}/sources")
                return response.json()

        except httpx.HTTPError:
            print(f"Ошибка при получении данных.")
            return []

    def put_news(self):
        """Отправляет новость в сервис базы данных."""
        try:
            with httpx.Client() as client:
                response = client.post(url=f"{self._database_url}/sources")
                return response.json()

        except httpx.HTTPError:
            print(f"Ошибка при отправке данных.")
            return []

database_service = DatabaseService()
print(database_service.get_rss_sources())
