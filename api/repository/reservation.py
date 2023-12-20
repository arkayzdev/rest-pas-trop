import sqlite3
from model.reservation import Reservation

class ReservationRepo:

    def create(self) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS reservation (id_reservation INTEGER PRIMARY KEY AUTOINCREMENT, start_date TIMESTAMP, end_date TIMESTAMP, price INTEGER, username CHAR(60))"
        cur.execute(query)
        conn.commit()
        conn.close()


    def insert(self, reservation: Reservation) -> None:
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


    def view(self, id_reservation: int) -> Reservation:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from reservation WHERE id_reservation=?"
        cur.execute(query, (id_reservation,))
        row = cur.fetchone()
        reservation = Reservation(row[0], row[1], row[2], row[3], row[4])
        return reservation
    

    def view_by_username(self, username: str) -> list[Reservation]:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from reservation WHERE username=?"
        cur.execute(query,(username, ))
        rows = cur.fetchall()
        if rows:
            reservations = [
                Reservation(row[0], row[1], row[2], row[3], row[4]) for row in rows
            ]
            return reservations
        return None

    def view_all(self) -> list[Reservation]:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from reservation"
        cur.execute(query)
        rows = cur.fetchall()
        reservations = [
            Reservation(row[0], row[1], row[2], row[3], row[4]) for row in rows
        ]
        return reservations
    

    def update(self,reservation: Reservation) -> None: 
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


    def delete(self, id_reservation: int) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM reservation WHERE id_reservation=?"
        cur.execute(query, (id,))
        conn.commit()
        conn.close()


    def delete_all(self) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM reservation"
        cur.execute(query)
        conn.commit()
        conn.close()
        




