import sqlite3
import os
from api.model.reservation import Reservation

class ReservationRepo:

    def create() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS reservation (id_reservation INTEGER PRIMARY KEY AUTOINCREMENT, start_date TIMESTAMP, end_date TIMESTAMP, price INTEGER, username TEXT)"
        cur.execute(query)
        conn.commit()
        conn.close()


    def insert(reservation: Reservation) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "INSERT INTO reservation (start_date, end_date, price, username) VALUES (?,?,?,?)"
        cur.execute(query, (
            reservation.start_date,
            reservation.end_date,
            reservation.price,
            reservation.username
        ))
        conn.commit()
        conn.close()


    def view_all() -> list[Reservation]:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from reservation"
        cur.execute(query)
        rows = cur.fetchall()

        reservations = [
            Reservation(row[0], row[1], row[2], row[3], row[4]) for row in rows
        ]
        return reservations
    

    def update(reservation: Reservation) -> None: 
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "UPDATE reservation SET start_date=?, end_date=?, price=?, username=?, WHERE id_reservation=?"
        cur.execute(query, (
            reservation.start_date,
            reservation.end_date,
            reservation.price,
            reservation.username,
            reservation.id_reservation
        ))
        conn.commit()
        conn.close()


    def delete(id_reservation: int) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM reservation WHERE id_reservation=?"
        cur.execute(query, (id,))
        conn.commit()
        conn.close()


    def deleteAll() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM reservation"
        cur.execute(query)
        conn.commit()
        conn.close()
        


# if not os.path.isfile('books.db'):
#     repo.create()
# repo.create()


