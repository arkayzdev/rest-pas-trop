from repository.apartment import ApartmentRepo
from model.apartment import Apartment

class ApartmentService:
    def __init__(self) -> None:
        self.apartment_repo = ApartmentRepo()
        
    def create(self, apartment: Apartment) -> None:
        self.apartment_repo.insert(apartment)    

    def get(self, id_apartment: int) -> Apartment:
        apartment = self.apartment_repo.view(id_apartment)
        if apartment:
            return apartment.apartment_to_json()
        return None
    
    def get_by_username(self, username: str) -> list[Apartment]:
        apartments = self.apartment_repo.view_by_username(username)
        if apartments:
            return [apartment.json_fmt() for apartment in apartments]
        return None

    def get_for_reservation(self, id_apartment: int) -> Apartment:
        apartment = self.apartment_repo.view(id_apartment)
        if apartment:
            return apartment.json_fmt()
        return None

    def get_all(self) -> list[Apartment]:
        apartments = self.apartment_repo.view_all()
        return [apartment.apartment_to_json() for apartment in apartments]

    def update(self, apartment: Apartment):
        self.apartment_repo.update(apartment)

    def delete(self, apartment: Apartment) -> None:
        self.apartment_repo.delete(apartment)

    def delete_all(self) -> None:
        self.apartment_repo.delete_all()

    def check_values(self, apartment: Apartment) -> bool:
        if not apartment.area.isdigit() or not apartment.max_people.isdigit():
            return False
        return True
    