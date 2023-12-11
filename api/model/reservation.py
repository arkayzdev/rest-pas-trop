import datetime

class Reservation:
    def __init__(self, id: int, start_date: datetime, end_date: datetime, price: int) -> None:
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
    