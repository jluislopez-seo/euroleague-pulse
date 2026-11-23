import os
import re
import json
import time
import hashlib
import feedparser
from datetime import datetime, timezone
from deep_translator import GoogleTranslator

FEEDS = [
    {"name": "Eurohoops", "url": "https://www.eurohoops.net/feed/", "lang": "en"},
    {"name": "BasketNews", "url": "https://basketnews.com/rss.xml", "lang": "en"},
    {"name": "Gigantes del Basket", "url": "https://www.gigantes.com/feed/", "lang": "es"},
    {"name": "Encestando", "url": "https://encestando.es/feed/", "lang": "es"},
    {"name": "SDNA", "url": "https://www.sdna.gr/rss.xml", "lang": "el"},
    {"name": "Gazzetta.gr", "url": "https://www.gazzetta.gr/rss", "lang": "el"},
    {"name": "TrendBasket", "url": "https://trendbasket.net/feed/", "lang": "tr"},
    {"name": "Euroleague.net", "url": "https://www.euroleaguebasketball.net/euroleague/news/rss/", "lang": "en"}
]

TARGET_LANGS = ["es", "en", "tr", "el"]

EUROLEAGUE_KEYWORDS = [
    "euroleague", "euroliga", "ευρωλίγκα", "real madrid", "barcelona", "baskonia",
    "valencia", "olympiacos", "panathinaikos", "fenerbahce", "fenerbahçe", "efes",
    "besiktas", "beşiktaş", "partizan", "zvezda", "estrella roja", "zalgiris",
    "žalgiris", "maccabi", "hapoel", "milan", "milano", "virtus", "bologna",
    "bayern", "asvel", "paris basketball", "dubai basketball", "monaco"
]

RUMOR_KEYWORDS = [
    "rumor", "rumour", "fichaje", "fichar", "interés", "interesado", "negocia",
    "acuerdo", "objetivo", "mercado", "salida", "rescisión", "signing", "target",
    "deal", "agreement", "transfer", "eyeing", "linked", "report", "reportedly",
    "φήμη", "μεταγραφή", "συμφωνία", "στόχος", "ενδιαφέρον",
    "söylenti", "transfer", "anlaşma", "ilgi", "iddia"
]

def clean_html(raw_html: str) -> str:
    text = re.sub(r"<[^>]*?>", " ", raw_html or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:240] + ("..." if len(text) > 240 else "")

def is_euroleague_related(text: str) -> bool:
    lower = text.lower()
    return any(kw in lower for kw in EUROLEAGUE_KEYWORDS)

def detect_category(text: str) -> str:
    lower = text.lower()
    return "rumor" if any(kw in lower for kw in RUMOR_KEYWORDS) else "official"

def translate_all_languages(text: str, source_lang: str) -> dict:
    result = {}
    if not text:
        return {lang: "" for lang in TARGET_LANGS}
    for lang in TARGET_LANGS:
        if lang == source_lang:
            result[lang] = text
        else:
            try:
                translated = GoogleTranslator(source="auto", target=lang).translate(text)
                result[lang] = translated or text
                time.sleep(0.15)
            except Exception:
                result[lang] = text
    return result

def main():
    os.makedirs("data", exist_ok=True)
    articles = []
    seen_urls = set()

    for feed_info in FEEDS:
        try:
            parsed = feedparser.parse(feed_info["url"])
            count = 0
            for entry in parsed.entries:
                if count >= 6:
                    break
                link = entry.get("link", "").strip()
                raw_title = clean_html(entry.get("title", ""))
                raw_summary = clean_html(entry.get("summary", "") or entry.get("description", ""))

                if not link or not raw_title or link in seen_urls:
                    continue

                combined_text = f"{raw_title} {raw_summary}"
                if feed_info["name"] != "Euroleague.net" and not is_euroleague_related(combined_text):
                    continue

                seen_urls.add(link)
                category = detect_category(combined_text)
                item_id = int(hashlib.md5(link.encode("utf-8")).hexdigest()[:8], 16)

                title_map = translate_all_languages(raw_title, feed_info["lang"])
                summary_map = translate_all_languages(raw_summary or raw_title, feed_info["lang"])

                articles.append({
                    "id": item_id,
                    "source": feed_info["name"],
                    "category": category,
                    "url": link,
                    "published": entry.get("published", datetime.now(timezone.utc).strftime("%d %b • %H:%M")),
                    "title": title_map,
                    "summary": summary_map
                })
                count += 1
        except Exception as exc:
            print(f"[WARN] Error leyendo {feed_info['name']}: {exc}")

    if articles:
        with open("data/news.json", "w", encoding="utf-8") as f:
            json.dump({
                "updated_at": datetime.now(timezone.utc).isoformat(),
                "total": len(articles),
                "items": articles
            }, f, ensure_ascii=False, indent=2)
        print(f"[OK] Guardadas {len(articles)} noticias multilingües en data/news.json")

if __name__ == "__main__":
    main()
