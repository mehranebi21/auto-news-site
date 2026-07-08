import feedparser
import json


rss = "https://feeds.bbci.co.uk/persian/rss.xml"


news = feedparser.parse(rss)


items=[]


for item in news.entries[:20]:

    items.append({

        "title":item.title,

        "description":
        item.get("summary",""),

        "link":
        item.link

    })


with open("news.json","w",
encoding="utf-8") as f:

    json.dump(
        items,
        f,
        ensure_ascii=False,
        indent=2
    )


print("News updated")
