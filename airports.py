from typing import List, NamedTuple, Tuple
import csv


class Airports:
    def __init__(self):
        self.data = self._load_data()

    def _load_data(self) -> List[Tuple]:
        with open('Airport_Codes_List.csv', mode='r') as infile:
            reader = csv.reader(infile)
            list_cities = [rows[0] for rows in reader]
            list_cities = list_cities[1:]
        with open('Airport_Codes_List.csv', mode='r') as infile:
            reader = csv.reader(infile)
            list_codes = [rows[2] for rows in reader]
            list_codes = list_codes[1:]
            self.data = list(zip(list_codes, list_cities))
            return self.data

