from api.repository.user import UserRepo
from api.model.user import User

class UserService:
    def __init__(self) -> None:
        self.user_repo = UserRepo()

    def create(self, user: User) -> None:
        self.user_repo.insert(user)    

    def get(self, username: str) -> User:
        return self.user_repo.view(username)
    
    def get_all(self) -> list[User]:
        users = self.user_repo.view_all()
        return [user.user_to_json() for user in users]

    def update(self, user: User) -> None:
        self.user_repo.update(user)

    def delete(self, user: User) -> None:
        self.user_repo.delete(user)

    def delete_all(self) -> None:
        self.user_repo.delete_all()

    def check_user(self, username: str) -> bool:
        if self.user_repo.get_id(username):
            return True
        return False
    