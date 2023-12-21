from repository.reservation import ReservationRepo
from model.reservation import Reservation
from service.apartment import ApartmentService

import exception.repository as ExRepo
import exception.service as ExServ


class ReservationService:
    def __init__(self) -> None:
        self.reservation_repo = ReservationRepo()
        self.apartment_service = ApartmentService()

    def create(self, reservation: Reservation) -> None:
        self.reservation_repo.insert(reservation)

    def get(self, id_reservation: int) -> Reservation:
        reservation = self.reservation_repo.view(id_reservation)
        return reservation.reservation_to_json()

    def get_all(self) -> list[Reservation]:
        reservations = self.reservation_repo.view_all()
        return [reservation.reservation_to_json() for reservation in reservations]

    def get_by_username(self, username: str) -> list[Reservation]:
        reservations = self.reservation_repo.view_by_username(username)
        if reservations:
            return [reservation.json_fmt() for reservation in reservations]
        return None

    def update(self, reservation: Reservation):
        self.reservation_repo.update(reservation)

    def delete(self, reservation: Reservation) -> None:
        self.reservation_repo.delete(reservation)

    def delete_all(self) -> None:
        self.reservation_repo.delete_all()

    def check_values(self, reservation: Reservation) -> bool:
        if not isinstance(reservation.start_date, str):
            return False
        if not isinstance(reservation.end_date, str):
            return False
        if not isinstance(reservation.price, int):
            return False
        return True
