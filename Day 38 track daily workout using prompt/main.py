import requests
import datetime as dt
import os

NUTRITION_APP_ID='a4b66173'
NUTRITION_API_KEY='6b4a93f06771c26f24770a6f843f7e46'

nutrition_endpoints="https://trackapi.nutritionix.com/v2/natural/exercise"

shetty_endpoints="https://api.sheety.co/52577846ef9bc903c6b74c744027b102/day38/workouts"

exercise_text = input("Enter the prompt : ")

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 183
AGE = 21

nutrition_parameters = {
    
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutrition_headers={

    "x-app-id":NUTRITION_APP_ID, #this key should be same 
    "x-app-key":NUTRITION_API_KEY #this key should be same 
}

response_nutrition=requests.post(url=nutrition_endpoints,json=nutrition_parameters,headers=nutrition_headers)
nutrition_result=response_nutrition.json()

#got the data from the nutrition API

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

bearer_headers={
    'Authorization': 'Bearer ZmVyZGVubzpkc2ZhZjMyNDA1MTkzMjQ='
}

for exercise in nutrition_result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(shetty_endpoints, json=sheet_inputs,auth=("ferdeno","dsfaf3240519324"),headers=bearer_headers)#this will post the data to excel

    print(sheet_response.text)

