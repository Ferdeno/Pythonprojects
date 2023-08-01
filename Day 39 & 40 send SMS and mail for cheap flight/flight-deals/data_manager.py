import requests


shetty_endpoints="https://api.sheety.co/52577846ef9bc903c6b74c744027b102/day39"

headers = {
        'Authorization': 'Bearer ZmVyZGVubzpkc2ZhZjMyNDA1MTkzMjQ=',
        'Content-Type': 'application/json'
    }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        shetty_response=requests.get(url=f"{shetty_endpoints}/prices",headers=headers)
        shetty_data=shetty_response.json()
        self.destination_data=shetty_data["prices"]

        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            response=requests.put(url=f"{shetty_endpoints}/prices/{city['id']}",json=new_data)
                

    def get_customer_emails(self):
        response=requests.get(url=f"{shetty_endpoints}/users",headers=headers)
        
        return response.json()['users']

