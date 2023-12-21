from repository.user import UserRepo
from service.user import UserService
from functions.hash import verify_hash
import base64

class AuthentificationService:
    def __init__(self) -> None:
        self.user_repo = UserRepo()
        self.user_service = UserService()

    def check_password(self, username: str, password: str) -> bool:
        user_password = self.user_repo.get_password(username)
        if verify_hash(password, user_password):
            print("True")
            return True
        print("False")
        return False
        

    def check_admin(self, username: str) -> bool:
        user_role = self.user_repo.get_role(username)
        if user_role == "Interne":
            return True
        return False
    

    def extract_credentials(self, authorization_header: base64) -> tuple:
        try:
            # Extract the encoded credentials part after "Basic "
            encoded_credentials = authorization_header.split(" ")[1]
            # Decode the Base64-encoded string to get username:password
            decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
            # Split username and password
            username, password = decoded_credentials.split(":", 1)
            return username, password
        except Exception as e:
            print(f"Error extracting credentials: {e}")
            return None, None
        

    def authenticate_admin(self, username:str, password: str) -> bool:
        if self.user_service.check_user(username):
            if self.check_password(username, password):
                if self.check_admin(username):
                    return True
        return False
