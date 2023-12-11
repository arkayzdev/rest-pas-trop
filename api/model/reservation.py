import datetime

class Reservation:
    def __init__(self, id_reservation: int, start_date: datetime, end_date: datetime, price: int, username: str) -> None:
        self.id = id_reservation
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.username = username
    