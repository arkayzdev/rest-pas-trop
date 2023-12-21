from flask import Blueprint, request, jsonify
from service.apartment import ApartmentService
from service.authentification import AuthentificationService
from service.user import UserService
from model.apartment import Apartment

import exception.service as ExServ
import exception.controller as ExCon


apartment_blueprint = Blueprint("apartment", __name__)

user_service = UserService()
service = ApartmentService()
auth = AuthentificationService()


@apartment_blueprint.route("/", methods=["POST"])
def create_apartment():
    try:
        req_data = request.get_json()
        all(
            key in req_data
            for key in ("username", "area", "max_people", "address", "availability")
        )
        apartment = Apartment(
            None,
            req_data["area"],
            req_data["max_people"],
            req_data["address"],
            bool(req_data["availability"]),
            req_data["username"],
        )
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)

    if not service.check_values(apartment):
        raise ExCon.ControllerException(400)
    if not user_service.check_user(apartment.username):
        raise ExCon.ControllerException(400)
    
    try:
        service.create(apartment)
    except Exception:
        raise ExCon.ControllerException(500)
    
    return jsonify({"message": "Success creating new apartment !"}), 200


@apartment_blueprint.route("/", methods=["GET"])
def get_apartments():
    try:
        jsonify(service.get_all())
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)
    return jsonify(service.get_all())


@apartment_blueprint.route("/<int:apartment_id>", methods=["GET"])
def get_apartment_id(apartment_id: int):
    try: 
        apartment = service.get(apartment_id)
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)
    if apartment:
        return jsonify(apartment)
    else:
        raise ExCon.ControllerException(404)


@apartment_blueprint.route("/<int:apartment_id>", methods=["PATCH"])
def update_apartment(apartment_id: int):
    try:
        req_data = request.get_json()
        if all(key in req_data for key in ("username", "area", "max_people", "address", "availability")):
            apartment = Apartment(apartment_id, req_data['area'], req_data['max_people'], req_data['address'], bool(req_data['availability']), req_data['username'])
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)
 
    if not service.check_values(apartment):
        raise ExCon.ControllerException(400)    
    if not service.get(apartment_id):
        raise ExCon.ControllerException(404)    
    
    if not user_service.check_user(apartment.username):
        raise ExCon.ControllerException(400)    

    service.update(apartment)
    return jsonify({"message": f"Successfully updated apartment: {apartment_id}"}), 200


@apartment_blueprint.route("/<int:apartment_id>", methods=["DELETE"])
def delete_apartment(apartment_id: int):
    if not service.get(apartment_id):
        raise ExCon.ControllerException(404)    

    service.delete(apartment_id)
    return jsonify({'message': f'Successfully deleted apartment: {apartment_id}'}), 200


@apartment_blueprint.route("/", methods=["DELETE"])
def delete_apartments():
    service.delete_all()
    return jsonify({"message": "All apartments deleted successfully"}), 200
