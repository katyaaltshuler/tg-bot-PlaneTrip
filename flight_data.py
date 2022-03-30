import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

API_KEY = os.getenv("API_KEY")
flight_endpoint = "https://tequila-api.kiwi.com/v2/search"

header = {
    "apikey": API_KEY
}


class FlightData:
    def __init__(self):
        self.data = {}
        self.arrival_city = ""
        self.departure_city = ""
        self.departure_date = ""
        self.departure_air = ""
        self.arrival_air = ""
        self.return_date = ""
        self.lowest_price = ""
        self.url = ""

    def get_prices(self, departure_code, arrival_code, dt_from, dt_return,
                   max_changes, days_min, days_max, price, currency):
        params = {
            "fly_from": departure_code,
            "fly_to": arrival_code,
            "date_from": dt_from,
            "date_to": dt_return,
            "max_stopovers": max_changes,
            "nights_in_dst_from": days_min,
            "nights_in_dst_to": days_max,
            "price_to": price,
            "curr": currency,
            "limit": 10
        }
        response = requests.get(url=f"{flight_endpoint}", headers=header, params=params)
        try:
            self.data = response.json()['data'][0]
        except LookupError as e:
            print(str(e))
            self.data = None
            return None

        self.arrival_city = self.data['cityTo']
        self.departure_city = self.data['cityFrom']
        self.departure_air = self.data['flyFrom']
        self.arrival_air = self.data['flyTo']
        self.departure_date = self.data['route'][0]['local_departure'].split("T")[0]
        self.lowest_price = self.data['price']
        self.url = self.data['deep_link']
        # try:
        #     self.return_date = self.data['route'][1]['local_departure'].split("T")[0]
        # except KeyError:
        #     pass

        return self.data
