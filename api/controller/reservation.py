from flask import Blueprint, request, jsonify
from service.reservation import ReservationService
from service.apartment import ApartmentService
from service.authentification import AuthentificationService
from service.user import UserService
from model.reservation import Reservation

import exception.service as ExServ
import exception.controller as ExCon

reservation_blueprint = Blueprint("reservation", __name__)

user_service = UserService()
service = ReservationService()
apartment_service = ApartmentService()
auth = AuthentificationService()


@reservation_blueprint.route("/", methods=["POST"])
def create_reservation():
    authorization_header = request.headers.get("Authorization")
    if not authorization_header or not authorization_header.startswith("Basic "):
        return jsonify({"message": "Authorization header missing or invalid"}), 401
    admin_username, admin_password = auth.extract_credentials(authorization_header)

    if admin_username == "" or admin_password == "":
        return jsonify({"message": "Invalid credentials format"}), 401

    try:
        req_data = request.get_json()
        all(
            key in req_data
            for key in ("start_date", "end_date", "price", "username", "id_apartment")
        )
        reservation = Reservation(
            None,
            None,
            None,
            req_data["price"],
            req_data["username"],
            req_data["id_apartment"]
        )

    except ExServ.ServiceException as e:
        print(e)
        raise ExCon.ControllerException(e.code)
    except Exception as e:
        print(e)
        raise ExCon.ControllerException(400)
    
    if not auth.authenticate_admin(admin_username, admin_password):
        if not auth.authenticate_user(admin_username, admin_password) or admin_username != reservation.username:
            raise ExCon.ControllerException(401)

    if not service.check_values(reservation):
        raise ExCon.ControllerException(400)
    
    if not apartment_service.get(reservation.id_apartment):
        raise ExCon.ControllerException(404)

    try:
        reservation.start_date = service.string_to_date(req_data["start_date"])
        reservation.end_date = service.string_to_date(req_data["end_date"])
    except Exception:
        raise ExCon.ControllerException(400)

    if not user_service.check_user(reservation.username):
        raise ExCon.ControllerException(404)

    service.create(reservation)
    return jsonify({"message": "Success creating new reservation!"}), 200


@reservation_blueprint.route("/", methods=["GET"])
def get_reservations():
    try:
        jsonify(service.get_all())
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)
    return jsonify(service.get_all())


@reservation_blueprint.route("/<int:reservation_id>", methods=["GET"])
def get_reservation(reservation_id: int):
    try:
        reservation = service.get(reservation_id)
        return jsonify(reservation)
    except ExServ.ServiceException as e:
        print(e)
        raise ExCon.ControllerException(e.code)
    except Exception as e:
        print(e)
        raise ExCon.ControllerException(500)    
         


@reservation_blueprint.route("/<int:reservation_id>", methods=["PATCH"])
def update_reservation(reservation_id: int):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header or not authorization_header.startswith("Basic "):
        return jsonify({"message": "Authorization header missing or invalid"}), 401
    admin_username, admin_password = auth.extract_credentials(authorization_header)

    if admin_username == "" or admin_password == "":
        return jsonify({"message": "Invalid credentials format"}), 401
    try:
        req_data = request.get_json()
        reservation = Reservation(
            None,
            req_data["apartment_id"],
            req_data["user_id"],
            req_data["start_date"],
            req_data["end_date"],
            None,
        )
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)
    
    if not auth.authenticate_admin(admin_username, admin_password):
        if not auth.authenticate_user(admin_username, admin_password) or admin_username != reservation.username:
            raise ExCon.ControllerException(401)

    if not service.check_values(reservation):
        raise ExCon.ControllerException(400)
    
    if not apartment_service.get(reservation.id_apartment):
        raise ExCon.ControllerException(404)

    try:
        service.update(reservation)
        return (
            jsonify({"message": f"Successfully updated reservation: {reservation_id}"}),
            200,
        )
    except Exception:
        raise ExCon.ControllerException(500)


@reservation_blueprint.route("/<int:reservation_id>", methods=["DELETE"])
def delete_reservation(reservation_id: int):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header or not authorization_header.startswith("Basic "):
        return jsonify({"message": "Authorization header missing or invalid"}), 401
    admin_username, admin_password = auth.extract_credentials(authorization_header)

    if admin_username == "" or admin_password == "":
        return jsonify({"message": "Invalid credentials format"}), 401
    try:
        reservation = service.get(reservation_id)
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)
    
    reservation_username = service.get_username(reservation_id)

    if not auth.authenticate_admin(admin_username, admin_password):
        if not auth.authenticate_user(admin_username, admin_password) or admin_username != reservation_username:
            raise ExCon.ControllerException(401)

    if not service.check_values(reservation):
        raise ExCon.ControllerException(400)
    
    if not apartment_service.get(reservation.id_apartment):
        raise ExCon.ControllerException(404)

    if reservation:
        service.delete(reservation_id)
        return (
            jsonify({"message": f"Successfully deleted reservation: {reservation_id}"}),
            200,
        )
    else:
        raise ExCon.ControllerException(404)


@reservation_blueprint.route("/", methods=["DELETE"])
def delete_reservations():
    try:
        service.delete_all()
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)
    return jsonify({"message": "All reservations deleted successfully"}), 200
