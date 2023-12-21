from repository.user import UserRepo
from service.reservation import ReservationService
from service.apartment import ApartmentService
from model.user import User

import exception.repository as ExRepo
import exception.service as ExServ


class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepo()
        self.reservation_service = ReservationService()
        self.apartment_service = ApartmentService()

    def create(self, user: User) -> None:
        try:
            self.user_repo.insert(user)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def get(self, username: str) -> dict:
        try:
            user = self.user_repo.view(username)
            user_json = user.user_to_json()
            user_json["apartment"] = self.apartment_service.get_by_username(username)
            user_json["reservation"] = self.reservation_service.get_by_username(
                username
            )
            return user_json
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def get_all(self) -> list[dict]:
        try:
            users = self.user_repo.view_all()
            users_json = [user.user_to_json() for user in users]
            for user_json in users_json:
                user_json["apartment"] = self.apartment_service.get_by_username(
                    user_json["username"]
                )
                user_json["reservation"] = self.apartment_service.get_by_username(
                    user_json["username"]
                )
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)
        return users_json

    def get_id(self, username: str):
        return self.user_repo.get_id(username)

    def update(self, user: User) -> None:
        try:
            self.user_repo.update(user)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete(self, user: User) -> None:
        try:
            self.user_repo.delete(user)
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def delete_all(self) -> None:
        try:
            self.user_repo.delete_all()
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def check_user(self, username: str) -> bool:
        try:
            if self.user_repo.get_id(username):
                return True
            # return False
        except ExRepo.RepositoryException as e:
            raise ExServ.ServiceException(e.code)
        except Exception:
            raise ExServ.ServiceException(500)

    def check_values(self, user: User) -> bool:
        if len(user.username) > 60:
            raise ExServ.ServiceException(500)
        if len(user.first_name) > 30:
            raise ExServ.ServiceException(500)
        if len(user.last_name) > 30:
            raise ExServ.ServiceException(500)
        return True
