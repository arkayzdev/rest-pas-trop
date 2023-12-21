import sqlite3
from passlib.hash import sha256_crypt

def hash_password(password: str) -> sha256_crypt:
    return sha256_crypt.using(rounds=5000).hash(password)

def verify_hash(password: str, hashed: sha256_crypt) -> bool:
    return sha256_crypt.verify(password, hashed)



conn = sqlite3.connect("database/rest_pas_trop.db")
cur = conn.cursor()
query = "INSERT INTO user (username, first_name, last_name, password, role) VALUES (?,?,?,?,?)"
cur.execute(
    query,
    (
        "admin",
        "adminfn",
        "adminln",
        hash_password("admin"),
        "Interne"
    ),
)
conn.commit()
conn.close()