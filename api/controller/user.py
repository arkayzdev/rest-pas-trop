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
    req_data = request.get_json()
    if all(
        key in req_data for key in ("username", "first_name", "last_name", "password")
    ):
        user = User(
            None,
            req_data["username"],
            req_data["first_name"],
            req_data["last_name"],
            req_data["password"],
            None,
        )
    else:
        return (
            jsonify({"message": "Arguments are not valid.", "error": "Bad Request"}),
            400,
        )

    if not service.check_values(user):
        return (
            jsonify({"message": "The size of the fields entered is not respected"}),
            400,
        )

    if service.check_user(user.username):
        return jsonify({"message": "The username you entered already exist"}), 403

    service.create(user)
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
        return jsonify({"message": "The username you entered does not exist"}), 400

    user = service.get(username)

    if user:
        return jsonify(user)


@user_blueprint.route("/<string:username>", methods=["PATCH"])
def update_user(username: str):
    req_data = request.get_json()
    if all(
        key in req_data for key in ("username", "first_name", "last_name", "password")
    ):
        user = User(
            None,
            req_data["username"],
            req_data["first_name"],
            req_data["last_name"],
            req_data["password"],
            None,
        )
    else:
        return (
            jsonify({"message": "Arguments are not valid.", "error": "Bad Request"}),
            400,
        )

    if not service.check_values(user):
        return (
            jsonify({"message": "The size of the fields entered is not respected"}),
            400,
        )

    if not service.check_user(username):
        return jsonify({"message": "This username does not exist"}), 400

    service.update(user, username)
    return jsonify({"message": f"Successfully updated user: {username}"}), 200


@user_blueprint.route("/<string:username>", methods=["DELETE"])
def delete_user(username: str):
    user = service.check_user(username)
    if user:
        service.delete(username)
        return jsonify({"message": f"Successfully deleted user: {username}"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


@user_blueprint.route("/", methods=["DELETE"])
def delete_users():
    service.delete_all()
    return jsonify({"message": "All users deleted successfully"}), 200
