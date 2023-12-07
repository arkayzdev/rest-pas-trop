import sqlite3
import os
from api.model.apartment import Apartment

class ApartmentRepo:

    def create() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS apartment (id INTEGER PRIMARY KEY AUTOINCREMENT, area INTEGER, max_people INTEGER, address TEXT, availability BOOLEAN)"
        cur.execute(query)
        conn.commit()
        conn.close()


    def insert(apartment: Apartment) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "INSERT INTO apartment (area, max_people, address, availability) VALUES (?,?,?,?)"
        cur.execute(query, (
            apartment.area,
            apartment.max_people,
            apartment.address,
            apartment.availability
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
            Apartment(row[0], row[1], row[2], row[3], True if row[4] == 1 else False) for row in rows
        ]
        return apartments
    

    def update(self, apartment: Apartment) -> None: 
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "UPDATE apartment SET area=?, max_people=?, address=?, availability=? WHERE id=?"
        cur.execute(query,
            apartment.area,
            apartment.max_people,
            apartment.address,
            apartment.availability)
        conn.commit()
        conn.close()


    def delete(id: int) -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM artworks WHERE id=?"
        cur.execute(query, (id,))
        conn.commit()
        conn.close()


    def deleteAll() -> None:
        conn = sqlite3.connect('database/rest_pas_trop.db')
        cur = conn.cursor()
        query = "DELETE FROM artworks"
        cur.execute(query)
        conn.commit()
        conn.close()
        
# apart = Apartment(None, 30,30,"28 a", True)

# repo = ApartmentRepo('database/rest_pas_trop.db')
# repo.insert(apart)
# print(repo.view_all())


# if not os.path.isfile('books.db'):
#     repo.create()
# repo.create()


