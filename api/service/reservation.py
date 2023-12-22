from repository.reservation import ReservationRepo
from model.reservation import Reservation
from service.apartment import ApartmentService
from repository.user import UserRepo
import exception.repository as ExRepo
import exception.service as ExServ
from datetime import datetime


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
     

    def get_all(self) -> list[Reservation]:
        try:
            reservations = self.reservation_repo.view_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception as e:
            raise ExServ.ServiceException(500)
        try:
            reservations_json = []
            for reservation in reservations:
                reservation_json = reservation.reservation_to_json()
                try :
                    reservation_json['apartment'] = self.apartment_service.get_for_reservation(reservation.id_apartment)
                except Exception as e:
                    print(e)
                reservation_json['user'] = self.user_repo.view(reservation.username).json_fmt()
                reservations_json.append(reservation_json)
            return reservations_json
        except Exception as e:
            print(e)



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

    

    def delete(self, id_reservation: Reservation) -> None:
        try:
            self.reservation_repo.delete(id_reservation)
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


    def string_to_date(self, date: str) -> datetime:
        try:
            date_obj = datetime.strptime(date, '%d-%m-%Y')
            return date_obj
        except ValueError:
            print(f"The string '{date}' is not a valid date.")
            raise ExServ.ServiceException(400)


    def check_date(self, reservation: Reservation):
        try:
            if not self.reservation_repo.view_by_date(reservation):
                return True
            else:
                raise ValueError("Already a reservation at this date.")

        except ValueError as e:
            return False

    def check_values(self, reservation: Reservation) -> bool:
        try:
            if reservation.price.isdigit():
                return True
            else:
                raise ValueError("The string contains more than just numbers.")
        except ValueError as e:
            return False
        
    def get_username(self, id_reservation: int):
        try :
            return self.reservation_repo.get_username(id_reservation)
        except Exception:
            return None
