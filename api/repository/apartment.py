import sqlite3
import os
from api.model.apartment import Apartment

class ApartmentRepo:

    def create() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS apartment (id_apartment INTEGER PRIMARY KEY AUTOINCREMENT, area INTEGER, max_people INTEGER, address TEXT, availability BOOLEAN, username TEXT)"
        cur.execute(query)
        conn.commit()
        conn.close()


    def insert(apartment: Apartment) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "INSERT INTO apartment (area, max_people, address, availability, username) VALUES (?,?,?,?,?)"
        cur.execute(query, (
            apartment.area,
            apartment.max_people,
            apartment.address,
            apartment.availability,
            apartment.username
            ))
        conn.commit()
        conn.close()


    def view_all() -> list[Apartment]:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "SELECT * from apartment"
        cur.execute(query)
        rows = cur.fetchall()

        apartments = [
            Apartment(row[0], row[1], row[2], row[3], True if row[4] == 1 else False, row[5]) for row in rows
        ]
        return apartments
    

    def update(apartment: Apartment) -> None: 
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "UPDATE apartment SET area=?, max_people=?, address=?, availability=?, username=? WHERE id_apartment=?"
        cur.execute(query,
            apartment.area,
            apartment.max_people,
            apartment.address,
            apartment.availability,
            apartment.username,
            apartment.id_apartment)
        conn.commit()
        conn.close()


    def delete(id_apartment: int) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM apartment WHERE id_apartment=?"
        cur.execute(query, (id,))
        conn.commit()
        conn.close()


    def deleteAll() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM apartment"
        cur.execute(query)
        conn.commit()
        conn.close()
        


