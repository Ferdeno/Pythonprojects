import requests
from twilio.rest import Client

API_KEY="69f04e4613056b159c2761a9d9e664d2"
API_ENDPOINT="https://api.openweathermap.org/data/2.5/onecall"

account_sid = 'AC6bc98690e6ce8d74525292f427bf3556'
auth_token = '8a823d6fe0b414575fcc52baeb8afc11'

params={
    "lat":25.24,
    "lon":73.54,
    "exclude":"current,daily,minutely",
    "appid":API_KEY
}

response=requests.get(API_ENDPOINT,params=params)

def umbrelaa(hours_count):
    for i in range(hours_count):
        print(response.json()["hourly"][i]["weather"][0]["id"])
        if response.json()["hourly"][i]["weather"][0]["id"] <700:
            return True
    return False



if umbrelaa(12):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="Ajay is good gay",
            from_='+15416973044',
            to="+919677749649"
    )
    print(message.status)
    
else:
    print("No need of Umbrella")