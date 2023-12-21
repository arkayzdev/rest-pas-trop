import sqlite3
from model.apartment import Apartment

import exception.repository as ExRepo


class ApartmentRepo:
    def create(self) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "CREATE TABLE IF NOT EXISTS apartment (id_apartment INTEGER PRIMARY KEY AUTOINCREMENT, area INTEGER, max_people INTEGER, address TEXT, availability BOOLEAN, username CHAR(60))"
            cur.execute(query)
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def insert(self, apartment: Apartment) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "INSERT INTO apartment (area, max_people, address, availability, username) VALUES (?,?,?,?,?)"
            cur.execute(
                query,
                (
                    apartment.area,
                    apartment.max_people,
                    apartment.address,
                    apartment.availability,
                    apartment.username,
                ),
            )
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def view(self, id_apartment: int) -> Apartment:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from apartment WHERE id_apartment=?"
            cur.execute(query, (id_apartment,))
            row = cur.fetchone()
            conn.close()
            if row:
                apartment = Apartment(
                    row[0], row[1], row[2], row[3], True if row[4] == 1 else False, row[5]
                )
                return apartment
            else:
                return None
        except Exception:
            raise ExRepo.RepositoryException(500)

    def view_by_username(self, username: str) -> list[Apartment]:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from apartment WHERE username=?"
            cur.execute(query, (username,))
            rows = cur.fetchall()
            if rows:
                apartments = [
                    Apartment(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        True if row[4] == 1 else False,
                        row[5],
                    )
                    for row in rows
                ]
                return apartments
            return None
        except Exception:
            raise ExRepo.RepositoryException(500)

    def view_all(self) -> list[Apartment]:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from apartment"
            cur.execute(query)
            rows = cur.fetchall()
            apartments = [
                Apartment(
                    row[0], row[1], row[2], row[3], True if row[4] == 1 else False, row[5]
                )
                for row in rows
            ]
        except Exception:
            raise ExRepo.RepositoryException(500)
        if not apartments:
            raise ExRepo.RepositoryException(204)
        return apartments

    def update(self, apartment: Apartment) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "UPDATE apartment SET area=?, max_people=?, address=?, availability=?, username=? WHERE id_apartment=?"
            cur.execute(
                query,
                (
                    apartment.area,
                    apartment.max_people,
                    apartment.address,
                    apartment.availability,
                    apartment.username,
                    apartment.id_apartment,
                ),
            )
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def delete(self, id_apartment: int) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM apartment WHERE id_apartment=?"
            cur.execute(query, (id_apartment,))
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)

    def delete_all() -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM apartment"
            cur.execute(query)
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)


    def delete_by_username(self, username: str) -> None:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "DELETE FROM apartment WHERE username=?"
            cur.execute(query, (username,))
            conn.commit()
            conn.close()
        except Exception:
            raise ExRepo.RepositoryException(500)