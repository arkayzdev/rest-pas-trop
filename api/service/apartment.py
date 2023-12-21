from repository.apartment import ApartmentRepo
from model.apartment import Apartment

import exception.repository as ExRepo
import exception.service as ExServ

class ApartmentService:
    def __init__(self) -> None:
        self.apartment_repo = ApartmentRepo()
        
    def create(self, apartment: Apartment) -> None:
        try:
            self.apartment_repo.insert(apartment)    
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def get(self, id_apartment: int) -> Apartment:
        try:
            apartment = self.apartment_repo.view(id_apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if apartment:
            return apartment.apartment_to_json()
        return None
    
    def get_by_username(self, username: str) -> list[Apartment]:
        try:
            apartments = self.apartment_repo.view_by_username(username)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if apartments:
            return [apartment.json_fmt() for apartment in apartments]
        return None

    def get_for_reservation(self, id_apartment: int) -> Apartment:
        try:
            apartment = self.apartment_repo.view(id_apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        if apartment:
            return apartment.json_fmt()
        return None

    def get_all(self) -> list[Apartment]:
        try:
            apartments = self.apartment_repo.view_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        return [apartment.apartment_to_json() for apartment in apartments]

    def update(self, apartment: Apartment):
        try:
            self.apartment_repo.update(apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete(self, apartment: Apartment) -> None:
        try:
            self.apartment_repo.delete(apartment)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete_all(self) -> None:
        try:
            self.apartment_repo.delete_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def check_values(self, apartment: Apartment) -> bool:
        if not apartment.area.isdigit() or not apartment.max_people.isdigit():
            return False
        return True
    