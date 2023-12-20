from repository.reservation import ReservationRepo
from model.reservation import Reservation

class ReservationService:
    def __init__(self) -> None:
        self.reservation_repo = ReservationRepo()

    def create(self, reservation: Reservation) -> None:
        self.reservation_repo.insert(reservation)    

    def get(self, id_reservation: int) -> Reservation:
        return self.reservation_repo.view(id_reservation)
    
    def get_all(self) -> list[Reservation]:
        return self.reservation_repo.view_all()

    def update(self, reservation: Reservation):
        self.reservation_repo.update(reservation)

    def delete(self, reservation: Reservation) -> None:
        self.reservation_repo.delete(reservation)

    def delete_all(self) -> None:
        self.reservation_repo.delete_all()

    def check_values(self, start_date: str, end_date: str, price: int) -> bool:
        if not isinstance(start_date, str):
            return False
        if not isinstance(end_date, str):
            return False
        if not isinstance(price, int):
            return False
        return True