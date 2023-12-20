from api.repository.user import UserRepo
from api.repository.reservation import ReservationRepo
from api.repository.apartment import ApartmentRepo 

user = UserRepo()
reservation = ReservationRepo()
apartment = ApartmentRepo()

tables = [user, reservation, apartment]
for table in tables:
    table.create()