class NewsEvent:
    def __init__(self, text, is_open_source=False, has_binary_blob=False, is_hardware=False, uses_javascript=False):
        self.text = text
        self.is_open_source = is_open_source
        self.has_binary_blob = has_binary_blob
        self.is_hardware = is_hardware
        self.uses_javascript = uses_javascript


# Бот
def stallman_bot(news_event):
    if news_event.is_open_source:
        return "ВЫ ДОЛЖНЫ НАЗЫВАТЬ ЭТО FREE SOFTWARE, А НЕ OPEN SOURCE!!1"
    elif news_event.has_binary_blob or news_event.is_hardware:
        return "ЭТО НЕДЕМОКРАТИЧНЫЙ ПРОПРИЕТАРНЫЙ КУСОК КРЕМНИЯ!"
    elif "Linux" in news_event.text:
        return "ИСПРАВЬТЕ НА GNU/LINUX СРОЧНО!"
    elif news_event.uses_javascript:
        return "LIBREJS ЗАБЛОКИРОВАЛ ЭТОТ ЗЛОБНЫЙ СКРИПТ, ВЫ СВОБОДНЫ!"
    else:
        return "ПОЖЕРТВУЙТЕ 5 ДОЛЛАРОВ В FSF И КУПИТЕ ФЛЕШКУ С НУЛЕВЫМ КОДОМ."


class NewsSystem:
    def __init__(self):
        self.feed = []

    def publish_news(self, news_event):
        """Публикует новость и пропускает её через бота StallmanBot."""
        commentary = stallman_bot(news_event)
        
        print(f"📰 Новость: {news_event.text}")
        print(f"💬 Реакция StallmanBot: {commentary}")
        print("-" * 50)
        
        self.feed.append({
            "event": news_event,
            "commentary": commentary
        })


# Пример использования системы:
if __name__ == "__main__":
    system = NewsSystem()

    # 1. Новость про Open Source
    system.publish_news(NewsEvent(
        text="Компания выпустила новый инструмент.",
        is_open_source=True
    ))

    # 2. Новость про Linux без приставки GNU
    system.publish_news(NewsEvent(
        text="Ядро Linux получило крупное обновление безопасности."
    ))

    # 3. Новость про железо/бинарный блоб
    system.publish_news(NewsEvent(
        text="Анонсирован новый процессор с закрытой прошивкой.",
        has_binary_blob=True
    ))

    # 4. Обычная нейтральная новость
    system.publish_news(NewsEvent(
        text="Сегодня отличная погода для написания кода дома."
    ))
