from repository.reservation import ReservationRepo
from model.reservation import Reservation
from service.apartment import ApartmentService
from repository.user import UserRepo
import exception.repository as ExRepo
import exception.service as ExServ


class ReservationService:
    def __init__(self) -> None:
        self.reservation_repo = ReservationRepo()
        self.apartment_service = ApartmentService()
        self.user_repo = UserRepo()

    def create(self, reservation: Reservation) -> None:
        try:
            self.reservation_repo.insert(reservation)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def get(self, id_reservation: int) -> Reservation:
        try:
            reservation = self.reservation_repo.view(id_reservation)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if reservation:
            reservation_json = reservation.reservation_to_json()
            reservation_json['apartment'] = self.apartment_service.get_for_reservation(reservation.id_apartment)
            reservation_json['user'] = self.user_repo.view(reservation.username).json_fmt()
            return reservation_json
        return None
     
    def get_for_apartment(id_apartment):
        try:
            reservation = self.reservation_repo.view_by_apartment(id_apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if apartment:
            return apartment.json_fmt()
        return None

    def get_all(self) -> list[Reservation]:
        try:
            reservations = self.reservation_repo.view_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        reservations_json = []
        for reservation in reservations:
            reservation_json = reservation.reservation_to_json()
            reservation_json['apartment'] = self.apartment_service.get_for_reservation(reservation.id_apartment)
            reservation_json['user'] = self.user_repo.view(reservation.username).json_fmt()
            reservations_json.append(reservation_json)
        return reservations_json



    def get_by_username(self, username: str) -> list[Reservation]:
        try:
            reservations = self.reservation_repo.view_by_username(username)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if reservations:
            return [reservation.json_fmt() for reservation in reservations]
        return None

    
    def get_by_apartment(self, id_apartment: str) -> list[Reservation]:
        try:
            reservations = self.reservation_repo.view_by_apartment(id_apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if reservations:
            return [reservation.json_fmt() for reservation in reservations]
        return None

    def update(self, reservation: Reservation):
        try:
            self.reservation_repo.update(reservation)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete(self, reservation: Reservation) -> None:
        try:
            self.reservation_repo.delete(reservation)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete_by_username(self, username: str):
        try:
            self.reservation_repo.delete_by_username(username)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)




    def delete_all(self) -> None:
        try:
            self.reservation_repo.delete_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def check_values(self, reservation: Reservation) -> bool:
        if not isinstance(reservation.start_date, str):
            return False
        if not isinstance(reservation.end_date, str):
            return False
        if not isinstance(reservation.price, int):
            return False
        return True
