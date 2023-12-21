from flask import Blueprint, request, jsonify
from service.user import UserService
from model.user import User
from service.authentification import AuthentificationService

import exception.service as ExServ
import exception.controller as ExCon

user_blueprint = Blueprint("user", __name__)
auth = AuthentificationService()
service = UserService()


@user_blueprint.route("/", methods=["POST"])
def create_user():
    try:
        req_data = request.get_json()
        all(
            key in req_data
            for key in ("username", "first_name", "last_name", "password")
        )
        user = User(
            None,
            req_data["username"],
            req_data["first_name"],
            req_data["last_name"],
            req_data["password"],
            None,
        )
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)

    if not service.check_values(user):
        raise ExCon.ControllerException(400)

    if service.check_user(user.username):
        raise ExCon.ControllerException(403)

    try:
        service.create(user)
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)

    return jsonify({"message": "Success creating new user !"}), 200


@user_blueprint.route("/", methods=["GET"])
def get_users():
    try:
        jsonify(service.get_all())
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(500)
    return jsonify(service.get_all())


@user_blueprint.route("/<string:username>", methods=["GET"])
def get_user(username):
    if not service.check_user(username):
        raise ExCon.ControllerException(404)

    try:
        user = service.get(username)

        if user:
            return jsonify(user)
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(503)


@user_blueprint.route("/<string:username>", methods=["PATCH"])
def update_user(username: str):
    try:
        req_data = request.get_json()
        if all(
            key in req_data
            for key in ("username", "first_name", "last_name", "password")
        ):
            user = User(
                None,
                req_data["username"],
                req_data["first_name"],
                req_data["last_name"],
                req_data["password"],
                None,
            )
    except ExServ.ServiceException as e:
        raise ExCon.ControllerException(e.code)
    except Exception:
        raise ExCon.ControllerException(400)

    if not service.check_values(user):
        raise ExCon.ControllerException(400)

    if not service.check_user(username):
        raise ExCon.ControllerException(400)

    service.update(user, username)
    return jsonify({"message": f"Successfully updated user: {username}"}), 200


@user_blueprint.route("/<string:username>", methods=["DELETE"])
def delete_user(username: str):
    user = service.check_user(username)
    if user:
        service.delete(username)
        return jsonify({"message": f"Successfully deleted user: {username}"}), 200
    else:
        raise ExCon.ControllerException(404)


@user_blueprint.route("/", methods=["DELETE"])
def delete_users():
    service.delete_all()
    return jsonify({"message": "All users deleted successfully"}), 200
