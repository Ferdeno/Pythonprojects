#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import *
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager=DataManager()
flight_search=FlightSearch()
shetty_data=data_manager.get_destination_data()
ORIGIN_CITY_IATA = "BLR"
notificationManager=NotificationManager()

if shetty_data[0]["iataCode"]=="":
    
    for row in shetty_data:
        row["iataCode"]=flight_search.get_destination_code(row["city"])
    

    data_manager.destination_data=shetty_data
    data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in shetty_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight and flight.price and flight.price < destination["lowestPrice"] :


        users = data_manager.get_customer_emails()
        emails = [row["gmail"] for row in users]
        names = [row["firstName"] for row in users]

        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs>0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # notificationManager.send_sms(message)
        
        # notificationManager.send_email(message,emails)
