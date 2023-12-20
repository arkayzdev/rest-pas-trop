import sqlite3
from model.user import User
from functions.hash import hash_password

import exception.repository as ExRepo


class UserRepo:
    def create(self) -> None:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, username CHAR(60), first_name CHAR(30), last_name CHAR(30), password CHAR(64), role CHAR(10) DEFAULT 'Client')"
        cur.execute(query)
        conn.commit()
        conn.close()

    def insert(self, user: User) -> None:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "INSERT INTO user (username, first_name, last_name, password) VALUES (?,?,?,?)"
        cur.execute(
            query,
            (
                user.username,
                user.first_name,
                user.last_name,
                hash_password(user.password),
            ),
        )
        conn.commit()
        conn.close()

    def view(self, username: str) -> User:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "SELECT * from user WHERE username=?"
        cur.execute(query, (username,))
        row = cur.fetchone()

        user = User(row[0], row[1], row[2], row[3], row[4], row[5])

        return user

    def view_all(self) -> list[User]:
        try:
            conn = sqlite3.connect("database/rest_pas_trop.db")
            cur = conn.cursor()
            query = "SELECT * from user"
            cur.execute(query)
            rows = cur.fetchall()

            users = [
                User(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows
            ]
            if not users:
                raise ExRepo.RepositoryException(
                    "No users found in the repository.",
                    404,
                )
        except Exception:
            raise ExRepo.RepositoryException(
                "A general database error occurred.",
                500,
            )
        return users

    def update(self, user: User) -> None:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "UPDATE user SET username=? first_name=?, last_name=?, password=?, role=? WHERE username=?"
        cur.execute(
            query,
            (
                user.username,
                user.first_name,
                user.last_name,
                hash_password(user.password),
                user.role,
            ),
        )
        conn.commit()
        conn.close()

    def delete(self, username: str) -> None:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "DELETE FROM user WHERE username=?"
        cur.execute(query, (username,))
        conn.commit()
        conn.close()

    def delete_all(self) -> None:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "DELETE FROM user"
        cur.execute(query)
        conn.commit()
        conn.close()

    def get_id(self, username: str) -> str:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "SELECT id WHERE username=?"
        cur.execute(query, (username,))
        conn.commit()
        conn.close()
        row = cur.fetchone()
        if row:
            return row[0]
        return None

    def get_password(self, username: str) -> str:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "SELECT password WHERE username=?"
        cur.execute(query, (username,))
        conn.commit()
        conn.close()
        row = cur.fetchone()
        return row[0]

    def get_role(self, username: str) -> str:
        conn = sqlite3.connect("database/rest_pas_trop.db")
        cur = conn.cursor()
        query = "SELECT role WHERE username=?"
        cur.execute(query, (username,))
        conn.commit()
        conn.close()
        row = cur.fetchone()
        return row[0]
