import json
import feedparser
from datetime import datetime
from deep_translator import GoogleTranslator

# Fuentes RSS oficiales de los principales medios de Euroliga
FEEDS = [
    {"name": "Eurohoops", "url": "https://www.eurohoops.net/feed/", "lang": "en"},
    {"name": "BasketNews", "url": "https://basketnews.com/rss.xml", "lang": "en"},
    {"name": "Gigantes del Basket", "url": "https://www.gigantes.com/feed/", "lang": "es"},
            "items": articles
        }, f, ensure_ascii=False, indent=2)

    # También actualiza data/schedule.json y data/standings.json para la barra lateral
    with open("data/schedule.json", "w", encoding="utf-8") as f:
        json.dump({"updated_at": datetime.utcnow().isoformat(), "rounds": []}, f, ensure_ascii=False, indent=2)

    with open("data/standings.json", "w", encoding="utf-8") as f:
        json.dump({"updated_at": datetime.utcnow().isoformat(), "table": []}, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
