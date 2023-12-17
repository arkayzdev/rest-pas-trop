from flask import Blueprint, request
from api.service.user import UserService

user_blueprint = Blueprint('user', __name__)

service = UserService

@user_blueprint.route('/', methods=['POST'])
def create_user():
    pass


@user_blueprint.route('/', methods=['GET'])
def get_users():
    pass


@user_blueprint.route('/<str:username>', methods=['GET'])
def get_user(username: str):
    pass


@user_blueprint.route('/<str:username>', methods=['PATCH'])
def update_user(username: str):
    pass


@user_blueprint.route('/<str:username>', methods=['DELETE'])
def delete_user(username: str):
    pass


@user_blueprint.route('/', methods=['DELETE'])
def delete_users():
    pass

