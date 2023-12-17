import os
from dotenv import load_dotenv

load_dotenv()

class User:
    def __init__(self, id: int, username: str, first_name: str, last_name:str, password: int, role: str) -> None:
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role
        
    def serialize(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def json_fmt(self):
        return {
            'user': {
                'username' : self.username,
                'url': f'{os.getenv("hostname")}{self.username}'
            }
        }