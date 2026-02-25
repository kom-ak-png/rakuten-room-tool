from flask import Flask
import requests

app = Flask(__name__)

APP_ID = "f2c7d495-1536-4184-a523-4adf0f6db0d1"

@app.route("/")
def home():

    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

    params = {
        "applicationId": APP_ID,
        "keyword": "美容",
        "sort": "-reviewCount",
        "hits": 10
    }

    res = requests.get(url, params=params)
    data = res.json()

    html = "<h1>楽天ROOM投稿候補</h1>"

    for item in data["Items"]:

        name = item["Item"]["itemName"]
        item_url = item["Item"]["itemUrl"]

        html += f"""
        <hr>
        <h3>{name}</h3>
        <a href="{item_url}">商品を見る</a>
        """

    return html
