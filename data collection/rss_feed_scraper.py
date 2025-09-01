import requests
#pip install requests
#pip install feedparser
import feedparser
import json

url="https://feeds.feedburner.com/ndtvnews-top-stories"
feed = feedparser.parse(url)
print(feed.keys())
print(feed['entries'][0])
feed_data={"articles":[]}
for entry in feed["entries"]:
    article = {
        "title": entry.get('title', ''),
        "link": entry.get('link', ''),
        "description": entry.get('summary', ''),
        "detail":entry.content[0].get('value','')
    }
    feed_data["articles"].append(article)
    
print(json.dumps(feed_data,indent=4))
print(json.dumps(feed['entries'][0],indent=4))

    