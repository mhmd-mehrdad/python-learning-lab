import os
import requests


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY
    }

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)

print(stock_response.status_code)

data = stock_response.json()
new_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in new_data.items()]
print(data_list)

yesterday_price = data["Time Series (Daily)"]["2026-07-16"]["4. close"]
print(yesterday_price)



before_yesterday_price = data["Time Series (Daily)"]["2026-07-15"]["4. close"]
print(before_yesterday_price)



difference = abs(float(before_yesterday_price) - float(yesterday_price))



difference_percentage =round((difference) / float(before_yesterday_price), 2) * 100
print(difference_percentage)



if difference_percentage >= 5:
    print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.



new_response = requests.get(NEWS_ENDPOINT)
print(new_response.status_code)
data = new_response.json()




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
