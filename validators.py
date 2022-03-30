from datetime import datetime
from typing import List, NamedTuple, Tuple
import exceptions
from airports import Airports
from flight_data import *
import re

flight_data = FlightData()
airports = Airports()
data = airports.data

CURRENCY = ['EUR', 'USD', 'GBP']

class Validators:
    def __init__(self):
        flight_type: str

    def check_flight_type(self, raw_message: str):
        return self._parse_flight_type(raw_message)

    def parse_first_message(self, raw_message):
        self.flight_type = self._parse_flight_type(raw_message)
        self.departure, self.departure_code, self.arrival, self.arrival_code = self._parse_direction(raw_message)
        self.max_changes = self._parse_max_changes(raw_message)

    def _parse_max_changes(self, raw_message):
        try:
            numbers = re.search(r'(\d+)', raw_message.lower())
            max_changes = int(numbers.group()) if numbers else 0
            return max_changes
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand number of changes. Please, try again")

    def _parse_flight_type(self, raw_message):
        try:
            x = re.search("round", raw_message.lower())
            flight_type = x.group() if x else "oneway"
            return flight_type
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand flight type. Please, try again")

    def _parse_direction(self, raw_message):
        try:
            route = re.findall(r'(\w+) to (\w+)', raw_message)[0]
            dest, arr = route
            for code_city in data:
                if dest.capitalize() in code_city[1]:
                    departure = code_city[1]
                    departure_code = code_city[0]
                    break
            for code_city in data:
                if arr.capitalize() in code_city[1]:
                    arrival = code_city[1]
                    arrival_code = code_city[0]
                    break
                elif arr.lower() == 'anywhere':
                    arrival = 'anywhere'
                    arrival_code = ''
            return departure, departure_code, arrival, arrival_code
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand direction. Please, try again")

    def parse_second_message(self, raw_message):
        self.from_date, self.return_date = self._parse_date_interval(raw_message)
        if self.flight_type == 'round':
            self.days_min, self.days_max = self._parse_minmax_days(raw_message)
        else:
            self.days_min, self.days_max = "", ""

    def _parse_date_interval(self, raw_message):
        try:
            k = re.findall(r'(\d\d/\d\d/\d\d\d\d+)-(\d\d/\d\d/\d\d\d\d+)', raw_message.replace(" ", ""))
            try:
                if k:
                    print(k)
                    from_date, return_date = k[0]
                    return from_date, return_date
                else:
                    k = re.findall(r'(\d\d/\d\d+)', raw_message.replace(" ", ""))
                    k = [item + f'/{self._get_now_year()}' for item in k]
                    from_date, return_date = k
                    return from_date, return_date
            except ValueError:
                print("I don't understand")
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand date interval. Please, try again")

    def _parse_minmax_days(self, raw_message):
        try:
            result = re.split('min', raw_message)
            minmax_dict = re.findall("\d+", result[1])
            days_min, days_max = minmax_dict
            return days_min, days_max
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand how many days of stay. Please, try again")

    def parse_last_message(self, raw_message):
        self.price, self.currency = self._parse_price(raw_message)

    def _parse_price(self, raw_message):
        try:
            regexp_result = re.match(r"([\d]+) (.*)", raw_message)
            for c in CURRENCY:
                if c in regexp_result.group(2).upper():
                    currency = c
            price = regexp_result.group(1)
            return price, currency
        except LookupError:
            raise exceptions.NotCorrectMessage(
                "Sorry, don't understand price. Please, try again")

    def _get_now_year(self) -> int:
        return datetime.now().year

    def pull_data_to_search(self):
        print(self.departure_code, self.arrival_code, self.from_date, self.return_date,
              self.max_changes, self.days_min, self.days_max, self.price, self.currency)
        self.data = flight_data.get_prices(self.departure_code, self.arrival_code, self.from_date, self.return_date,
                                           self.max_changes, self.days_min, self.days_max, self.price, self.currency)
        if self.data is None:
            return None
        else:
            return (self.flight_type, flight_data.departure_city, flight_data.departure_air, flight_data.arrival_city,
                    flight_data.arrival_air, flight_data.departure_date, flight_data.lowest_price,
                    self.currency.upper(),
                    flight_data.url)
