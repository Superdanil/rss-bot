import time

import feedparser
import schedule

from monitor.database_service import database_service


def parse_rss():
    rss_sources = database_service.get_rss_sources()
    news_items = []
    for source in rss_sources:
        parsed_source = feedparser.parse(source)

        if parsed_source.bozo:
            print(f"Ошибка при парсинге {source}: {parsed_source.bozo_exception}")
            continue

        print(f"Заголовки из {source}:")
        for entry in parsed_source.entries:
            news_item = {'title': entry.title, 'link': entry.link}
            news_items.append(news_item)
            print(f"- {news_item['title']} {news_item['link']}")


# if __name__ == "__main__":
#     parse_rss()


if __name__ == "__main__":
    # Запланировать выполнение функции раз в минуту
    schedule.every(5).seconds.do(parse_rss)
    while True:
        schedule.run_pending()
        # time.sleep(1)
