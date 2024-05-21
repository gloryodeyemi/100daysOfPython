import math
import requests
from twilio.rest import Client
import os

# Stock API details
STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')

# News API details
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

# Twilio details
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

# parameters for getting the stock data
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# get the stock data for Tesla
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]  # convert stock data to a list
print(stock_data)

# get the closing price for yesterday and the day before
yesterday_price = float(stock_data_list[0]["4. close"])
day_before_price = float(stock_data_list[1]["4. close"])

# find the difference between prices
price_diff = abs(yesterday_price - day_before_price)
percentage_diff = (price_diff / yesterday_price) * 100

print(f"Yesterday's price: {yesterday_price}\n"
      f"Day before price: {day_before_price}\n"
      f"Price difference: {price_diff}\n"
      f"Percentage difference: {percentage_diff}\n"
      f"*****************************************\n")

# parameters for getting the news data
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# get the news data
if percentage_diff > 1:
    # get the news data for Tesla
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]
    print(f"{news_data}\n*****************************************\n")

    news_data_titles = [data["title"] for data in news_data]
    news_data_desc = [data["description"] for data in news_data]
    print(f"Titles: {news_data_titles}\nDescriptions: {news_data_desc}\n*****************************************\n")

    # send news as SMS using Twilio
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for idx in range(3):
        message = client.messages \
            .create(
                body=f"TSLA: 🔺{math.ceil(percentage_diff)}%\nHeadline: {news_data_titles[idx]}\n"
                     f"Brief: {news_data_desc[idx]}",
                from_='*****',
                to='******'
            )
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
