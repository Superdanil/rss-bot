import feedparser
from typing import List, Dict


def fetch_rss_feed(url: str) -> List[Dict[str, str]]:
    """
    Парсит RSS-ленту по заданному URL и возвращает список новостей.

    :param url: URL RSS-ленты.
    :return: Список словарей с новостями.
    """
    feed = feedparser.parse(url)  # Парсим RSS-ленту
    news_items = []

    # Проходим по всем записям в ленте
    for entry in feed.entries:
        news_item = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if 'published' in entry else None,
            'summary': entry.summary if 'summary' in entry else None,
        }
        news_items.append(news_item)

    return news_items


# Пример использования функции
if __name__ == "__main__":
    url = "https://iz.ru/xml/rss/all.xml"  # Замените на URL вашей RSS-ленты
    news = fetch_rss_feed(url)
    for item in news:
    # print(f"Title: {item['title']}\nLink: {item['link']}\nPublished: {item['published']}\n")
        print(item)
