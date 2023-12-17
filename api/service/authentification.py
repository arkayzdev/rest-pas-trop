from api.repository.user import UserRepo
from api.service.user import UserService
import hashlib

class AuthentificationService:
    def __init__(self) -> None:
        self.user_repo = UserRepo
        self.user_service = UserService

    def check_password(self, username: str, password: str) -> int:
        user_password = self.user_repo.get_password(username)
        if hashlib.sha512(password.encode('UTF-8')) == user_password:
            return 1
        return 0
        
    def check_admin(self, username: str) -> int:
        user_role = self.user_repo.get_role(username)
        if user_role == "Interne":
            return 1
        return 0