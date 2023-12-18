from api.repository.apartment import ApartmentRepo
from api.model.apartment import Apartment

class ApartmentService:
    def __init__(self) -> None:
        self.apartment_repo = ApartmentRepo()
        
    def create(self, apartment: Apartment) -> None:
        self.apartment_repo.insert(apartment)    

    def get(self, id_apartment: int) -> Apartment:
        return self.apartment_repo.view(id_apartment)
    
    def get_by_username(self, username: str) -> list[Apartment]:
        return self.apartment_repo.view_by_username(username)
    
    def get_all(self) -> list[Apartment]:
        return self.apartment_repo.view_all()

    def update(self, apartment: Apartment):
        self.apartment_repo.update(apartment)

    def delete(self, apartment: Apartment) -> None:
        self.apartment_repo.delete(apartment)

    def delete_all(self) -> None:
        self.apartment_repo.delete_all()