import requests
import dotenv
import os
from datetime import date


dotenv.load_dotenv()



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
# r = requests.get(url)
# data = r.json()


# URL = 'https://www.alphavantage.co/query?'


STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
TIME_SERIES = 'TIME_SERIES_DAILY'
API_KEY = os.getenv("ALPHAVANTAGE")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# TODAYS_DATE = date.today().strftime("%Y-%m-%d")
# print(TODAYS_DATE)
TODAYS_DATE = '2026-05-30'
stocks_params = {
    'function': TIME_SERIES,
    'symbol': STOCK_NAME,
    'apikey':API_KEY,
}

# https://newsapi.org/v2/everything?q=tesla&from=2026-04-30&sortBy=publishedAt&apiKey=729f32ee673b494198c9a315a58158ee
news_params = {
    'q': STOCK_NAME,
    'from': TODAYS_DATE,
    'apiKey': NEWS_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stocks_params)
response.raise_for_status()
data = response.json()

previuos_day = []

time_series = data['Time Series (Daily)']
# # todays = time_series.keys()
# todays = time_series['2026-05-29']['4. close']
# # print(todays)
# for d in range(0, 2):
#     pass
#     # print(time_series[d])
#     # previuos_day.append(time_series[d]['4. close'])
#     # print(previuos_day)
# # print(previuos_day)


day_data = [value for (key, value) in time_series.items()]
# yesterday = float(day_data[1]['4. close'])
# day_before_yesterday = float(day_data[2]['4. close'])
yesterday = float(275.56)
day_before_yesterday = float(215.67)
# print(f"Yesterday's value = {yesterday}; Day_Before_Yesterday = {day_before_yesterday}")
positive_difference = abs(((yesterday - day_before_yesterday)/day_before_yesterday)*100)
if positive_difference > 5:
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    news_data = news_response.json()
    first_articles = news_data['articles'][:3]
    # head_lines = 
    print(first_articles)
# print(positive_difference)

# news_response = 

# print(data)

# datetime.today().strftime('%Y-%m-%d')


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

