import requests
import math
import html
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "T3SLIUYQK7QSE758"
NEWS_API_KEY = "909739602ebc4f4f8b89e9ecef476a70"
account_sid = "ACe4331a112d51a273a84d5eff6008cfac"
auth_token = os.environ.get("AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get("https://www.alphavantage.co/query", stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

price_yesterday = float(stock_data_list[0]["4. close"])
price_day_before_yest = float(stock_data_list[1]["4. close"])
price_change = (price_day_before_yest-price_yesterday)/price_yesterday * 100

if math.fabs(price_change) >= 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_response.raise_for_status()
    top_three_list = news_response.json()['articles'][:3]

    # Send a separate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)
    for article in top_three_list:
        message_text = f"{STOCK}: {round(price_change, 2)}%\nHeadline: {article['title']}\nBrief: {html.unescape(article['description'])}"
        print(message_text)
        message = client.messages.create(
            to="+17188699083",
            from_="+16204224537",
            body=message_text
        )



