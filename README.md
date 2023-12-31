#rest-pas-trop
Bienvenue sur l'API RestPaTrop, une api crée pour la solution logicielle d'une entreprise de locations d'appartements à court terme !
Notre API est codée en Python avec le framework Flask.

=== Sommaire ===
1. [Authentication]
2. [Base URL]
3. [Endpoints]
4. [Error Handling]
5. [Examples]
6. [Contact Us]

===== [Authentification] =====
Basic:
    - Admin:    
        Username : admin
        Password : admin
    - Customer: 
        Username : custom
        Password : custom

===== [Base URL] =====
http://127.0.0.1:5000/api/

====== [Endpoints] ======

### Utilisateurs ###

# Liste tout les utilisateurs
./user [GET] 
# Renvoi les informations d'un utilisateur
./user/<string:username> [GET]
# Envoi une requête de création de donnée
./user [POST]
body
{
    "first_name": "Jean",
    "last_name": "Dubois",
    "username": "DuJeandin",
    "password": "Jardin"
}
# Envoi une requête pour supprimer tous les utilisateurs
./user [DELETE]
# Envoi une requête pour supprimer un utilisateur
./user/<string:username> [DELETE]
# Envoi une requête pour corriger les données d'un utilisateur
./user/<string:username> [PATCH]

### Apartment ###

# Liste tous les appartements
./apartment [GET] 
# Renvoi les informations d'un appartement
./apartment/<int:apartment_id> [GET]
# Envoi une requête de création de donnée
./apartment [POST]
body{
    "username": "PaulGbas",
    "area": "80",
    "max_people": "9",
    "address" : "8 Rue Giroud",
    "availability" : "True"
}
# Envoi une requête pour supprimer tous les appartements
./apartment [DELETE]
# Envoi une requête pour supprimer un apartement
./apartment/<int:apartment_id> [DELETE]
# Envoi une requête pour corriger les données d'un apartement
./apartment/<int:apartment_id> [PATCH]

## Reservation ###

# Liste tous les reservations
./reservation [GET] 
# Renvoi les informations d'une réservation
./reservation/<int:reservation_id> [GET]
# Envoi une requête de création de donnée
./reservation [POST]
body{
    "start_date": "08-12-2023",
    "end_date": "03-12-2023",
    "price" : "120",
    "username" : "Azymof",
    "id_apartment" : "2"
}
# Envoi une requête pour supprimer tous les réservations
./reservation [DELETE]
# Envoi une requête pour supprimer une réservation
./reservation/<int:reservation_id> [DELETE]
# Envoi une requête pour corriger les données d'une réservation
./reservation/<int:reservation_id> [PATCH]

===== [Error Handling] =====
# Exemple d'un retour erreur géré par exceptions
body 
{
    "code": 400,
    "error": "Bad Request",
    "error_description": "Bad request syntax or unsupported method"
}

===== [Examples] =====
# http://127.0.0.1:5000/api/user/ [GET]
output body[
    {
        "apartment": [
            {
                "id_apartment": 2,
                "url": "http://127.0.0.1:5000/apartment/2"
            }
        ],
        "first_name": "goat",
        "last_name": "tié",
        "reservation": null,
        "username": "kpru"
    },
    {
        "apartment": null,
        "first_name": "goat",
        "last_name": "tié",
        "reservation": null,
        "username": "arkayz"
    },
    {
        "apartment": null,
        "first_name": "adminfn",
        "last_name": "adminln",
        "reservation": null,
        "username": "admin"
    },
]

# http://127.0.0.1:5000/api/apartment/ [POST]
input body{
  "username": "kpru",
  "area": "111",
  "max_people": "21",
  "address" : "coucou",
  "availability" : true
}
Basic Auth{
    username : admin
    password : admin
}
output body{
    "message": "Success creating new apartment !"
}

# http://127.0.0.1:5000/api/reservation/1
Basic Auth{
    username : DuJeanDin
    password : Jardin
}
output body{
    "code": 401,
    "error": "Unauthorized",
    "error_description": "No permission -- see authorization schemes"
}

===== [Contact Us] =====
# Zhuang Franck
email@ges : -
discord : -

# Vauloup Gautier
email@ges : -
discord : -

# Huang Frédéric
email@ges : fhuang2@myges.fr
discord : hisshiden 