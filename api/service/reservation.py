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
        if reservation:
            reservation_json = reservation.reservation_to_json()
            reservation_json['apartment'] = self.apartment_service.get_for_reservation(reservation.id_apartment)
            return reservation_json
        return None
     
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

    def delete(self, id_reservation) -> None:
        self.reservation_repo.delete(id_reservation)

    def delete_by_username(self, username: str):
        self.reservation_repo.delete_by_username(username)

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
