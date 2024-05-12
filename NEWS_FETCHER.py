import requests
import json

query = input("What type of news are you interested in...= ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-03-06&sortBy=publishedAt&apiKey=f97df279a0884639a73bf93f47cbfd0f"
r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------")
