import sqlite3
from model.reservation import Reservation

import exception.repository as ExRepo


class ReservationRepo:
    def create(self) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "CREATE TABLE IF NOT EXISTS reservation (id_reservation INTEGER PRIMARY KEY AUTOINCREMENT, start_date TIMESTAMP, end_date TIMESTAMP, price INTEGER, username CHAR(60), id_apartment INTEGER)"
            cur.execute(query)
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def insert(self, reservation: Reservation) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "INSERT INTO reservation (start_date, end_date, price, username, id_apartment) VALUES (?,?,?,?,?)"
            cur.execute(
                query,
                (
                    reservation.start_date,
                    reservation.end_date,
                    reservation.price,
                    reservation.username,
                    reservation.id_apartment
                ),
            )
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def view(self, id_reservation: int) -> Reservation:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from reservation WHERE id_reservation=?"
            cur.execute(query, (id_reservation,))
            row = cur.fetchone()

            reservation = Reservation(row[0], row[1], row[2], row[3], row[4], row[5])
        except Exception:
            raise ExRepo.RepositoryException(500)
        else:
            if not reservation:
                raise ExRepo.RepositoryException(404)
            return reservation

    def view_by_username(self, username: str) -> list[Reservation]:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from reservation WHERE username=?"
            cur.execute(query, (username,))
            rows = cur.fetchall()
            conn.close()
            if rows:
                reservations = [
                    Reservation(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows
                ]
                return reservations
        except Exception:
            raise ExRepo.RepositoryException(500)
        return None

    def view_by_apartment(self, id_apartment):
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from reservation WHERE id_apartment=?"
            cur.execute(query, (username,))
            rows = cur.fetchall()
            conn.close()
            if rows:
                reservations = [
                    Reservation(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows
                ]
                return reservations
        except Exception:
            raise ExRepo.RepositoryException(500)
        return None

    def view_all(self) -> list[Reservation]:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from reservation"
            cur.execute(query)
            rows = cur.fetchall()
            reservations = [
                Reservation(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows
            ]
        except Exception:
            raise ExRepo.RepositoryException(500)
        if not reservations:
            raise ExRepo.RepositoryException(204)
        return reservations

    def update(self, reservation: Reservation) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "UPDATE reservation SET start_date=?, end_date=?, price=?, username=?, id_apartment=? WHERE id_reservation=?"
            cur.execute(
                query,
                (
                    reservation.start_date,
                    reservation.end_date,
                    reservation.price,
                    reservation.username,
                    reservation.id_apartment,
                    reservation.id_reservation,
                ),
            )
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def delete(self, id_reservation: int) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM reservation WHERE id_reservation=?"
            cur.execute(query, (id,))
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def delete_all(self) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM reservation"
            cur.execute(query)
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def delete_by_username(self, username) -> None:
         try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM reservation WHERE username=?"
            cur.execute(query,(username, ))
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)