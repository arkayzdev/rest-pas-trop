from repository.user import UserRepo
from repository.reservation import ReservationRepo
from repository.apartment import ApartmentRepo

user = UserRepo()
reservation = ReservationRepo()
apartment = ApartmentRepo()

tables = [user, reservation, apartment]
for table in tables:
    table.create()
