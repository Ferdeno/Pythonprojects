import requests

# reponse=requests.get(url="http://api.open-notify.org/iss-now.json")

# reponse.raise_for_status()

# data=reponse.json()["iss_position"]
# print(data)

parameter={
        "lat":20.593683,
        "lng":78.962883,
        "formatted":0

    }

response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)
print(response.raise_for_status())
print(response.json())