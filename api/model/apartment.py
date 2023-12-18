import os
from dotenv import load_dotenv

load_dotenv()

class Apartment:
    def __init__(self, id_apartment: int, area: int, max_people: int, address: str, availability: bool, username: str) -> None:
        self.id_apartment = id_apartment
        self.area = area
        self.max_people = max_people
        self.address = address
        self.availability = availability
        self.username = username


    def serialize(self):
        return {
            'id_apartment': self.id_apartment,
            'area': self.area,
            'max_people': self.max_people,
            'address': self.address,
            'availability': self.availability
        }
    

    def json_fmt(self):
        return {
        'apartment': {
            'id_apartment' : self.id_apartment,
            'url': f'{os.getenv("hostname")}apartment/{self.id_apartment}'
        }
    }