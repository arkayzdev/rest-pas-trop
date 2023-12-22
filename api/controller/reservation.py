from flask import Blueprint, request, jsonify
from service.reservation import ReservationService
from service.authentification import AuthentificationService
from service.user import UserService
from model.reservation import Reservation

import exception.service as ExServ
import exception.controller as ExCon

reservation_blueprint = Blueprint("reservation", __name__)

user_service = UserService()
service = ReservationService()
auth = AuthentificationService()


@reservation_blueprint.route("/", methods=["POST"])
def create_reservation():
    try:
        authorization_header = request.headers.get("Authorization")
        if not authorization_header or not authorization_header.startswith("Basic "):
            return jsonify({"message": "Authorization header missing or invalid"}), 401
        username, password = auth.extract_credentials(authorization_header)

        if username == "" or password == "":
            return jsonify({"message": "Invalid credentials format"}), 401

        if not auth.authenticate_user(username, password):
            return jsonify({"message": "Invalid username or password"}), 401

        req_data = request.get_json()
        reservation = Reservation(
            None,
            req_data["start_date"],
            req_data["end_date"],
            req_data["price"],
            req_data["username"],
            None,
        )
    except ExServ.ServiceException as e:
        print(e)
        raise ExCon.ControllerException(e.code)
    except Exception as e:
        print(e)
        raise ExCon.ControllerException(400)
   
    if not service.check_values(reservation):
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
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)
    if reservation:
        return jsonify({"reservation": reservation})
    else:
        return jsonify({"message": "Reservation not found"}), 404


@reservation_blueprint.route("/<int:reservation_id>", methods=["PATCH"])
def update_reservation(reservation_id: int):
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
    
    service.update(reservation)
    return (
        jsonify({"message": f"Successfully updated reservation: {reservation_id}"}),
        200,
    )


@reservation_blueprint.route("/<int:reservation_id>", methods=["DELETE"])
def delete_reservation(reservation_id: int):
    try:
        reservation = service.get(reservation_id)
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)
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
