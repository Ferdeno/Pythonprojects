import requests

from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT="https://www.alphavantage.co/query"
STOCK_ALPHAVANTAGE_API_KEY="5UJ388VLFKC4NJ1T"

params={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":STOCK_ALPHAVANTAGE_API_KEY
}
response=requests.get(STOCK_ENDPOINT,params=params)
data=response.json()

data_list=[value for key,value in data["Time Series (Daily)"].items()]
yesterday_data=float(data_list[0]["4. close"])
day_before_yesterday_data=float(data_list[1]["4. close"])
# print(data_list)


# date=((dt.datetime.today() - dt.timedelta(days=1)).date())

# yesterday_date =date-dt.timedelta(days=1)

# day_before_yesterday_date =date - dt.timedelta(days=2)

# yesterday_data=float(data["Time Series (Daily)"][f"{yesterday_date}"]["4. close"])
# day_before_yesterday_data=float(data["Time Series (Daily)"][f"{day_before_yesterday_date}"]["4. close"])

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


NEWS_ENDPOINT="https://newsapi.org/v2/everything"
NEWS_API_KEY="0909c3c225bc455fb5b96f3621429312"

percentage=abs((yesterday_data-day_before_yesterday_data)/day_before_yesterday_data)*100

if percentage>0:
    news_params={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_params)
    news_data=news_response.json()["articles"][:3]
    

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    formatted_news=[f"Headline : {i['title']},Brief : {i['description']}"for i in news_data]
    TWILIO_SID = 'AC6bc98690e6ce8d74525292f427bf3556'
    TWILIO_TOKEN = '8a823d6fe0b414575fcc52baeb8afc11' 
    client = Client(TWILIO_SID,TWILIO_TOKEN)
    for i in formatted_news:
        print(i)
        message = client.messages.create(
                body=i,
                from_='+15416973044',
                to="+919677749649"
        )
        print(message.status)
## STEP 3: Use https://www.twilio.com

# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

