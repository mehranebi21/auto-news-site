import feedparser
import json


rss = "https://feeds.bbci.co.uk/persian/rss.xml"

feed = feedparser.parse(rss)


news=[]


for item in feed.entries[:20]:

    image="https://via.placeholder.com/800x450?text=Milad+News"


    if "media_content" in item:
        image=item.media_content[0]["url"]

    elif "media_thumbnail" in item:
        image=item.media_thumbnail[0]["url"]


    news.append({

        "title": item.title,

        "description":
        item.get("summary",""),

        "link":
        item.link,

        "image":
        image

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


print("updated")
