import feedparser
import json
from bs4 import BeautifulSoup


rss = "https://feeds.bbci.co.uk/persian/rss.xml"


feed = feedparser.parse(rss)


news = []


for item in feed.entries[:30]:

    title = item.get("title","")

    summary = item.get("summary","")

    # حذف تگ های HTML
    summary = BeautifulSoup(
        summary,
        "html.parser"
    ).get_text()


    image = ""

    # پیدا کردن عکس
    if "media_content" in item:

        image = item.media_content[0].get("url","")


    if not image:

        image = "https://via.placeholder.com/900x500?text=Milad+News"



    news.append({

        "title": title,

        "description": summary,

        "content": summary,

        "image": image

    })




with open(
    "news.json",
    "w",
    encoding="utf-8"
) as f:


    json.dump(
        news,
        f,
        ensure_ascii=False,
        indent=2
    )



print("News updated")
