class Apartment:
    def __init__(self, id_apartment: int, area: int, max_people: int, address: str, availability: bool, username: str) -> None:
        self.id_apartment = id_apartment
        self.area = area
        self.max_people = max_people
        self.address = address
        self.availability = availability
        self.username = username


    