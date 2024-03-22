import requests
from bs4 import BeautifulSoup
import json

url = "https://finviz.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
headlines = soup.find(
    "table", class_="styled-table-new is-rounded is-condensed hp_news-table table-fixed"
)
article_names = headlines.find_all("a")
timestamps = headlines.find_all("td", class_="text-center")

data = {"headlines": []}
for article, timestamp in zip(article_names, timestamps):
    article_name = article.text
    article_link = article["href"]
    article_timestamp = timestamp.text
    data["headlines"].append(
        {
            "article_name": article_name,
            "article_link": article_link,
            "article_timestamp": article_timestamp,
        }
    )
    with open("news-dump.json", "w") as f:
        dump = json.dumps(data, indent=4)
        f.write(dump)
