import datetime
from dotenv import load_dotenv
import os
load_dotenv()

class Reservation:
    def __init__(self, id_reservation: int, start_date: datetime, end_date: datetime, price: int, username: str, id_apartment: str) -> None:
        self.id_reservation = id_reservation
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.username = username
        self.id_apartment = id_apartment
    
    
    def reservation_to_json(self):
        return {
            'id_reservation': self.id_reservation,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'price': self.price
        }
    

    def json_fmt(self):
        return {
            'id_reservation': self.id_reservation,
            'url': f'{os.getenv("hostname")}reservation/{self.id_reservation}'
            
        }