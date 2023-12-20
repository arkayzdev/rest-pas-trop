from flask import Blueprint, request, jsonify
from service.user import UserService
from model.user import User
from service.authentification import AuthentificationService

user_blueprint = Blueprint('user', __name__)
auth = AuthentificationService()
service = UserService()

@user_blueprint.route('/', methods=['POST'])
def create_user():
    req_data = request.get_json()
    user = User(None, req_data['username'], req_data['first_name'], req_data['last_name'], req_data['password'], None)
    print(service.create(user))
    #     return jsonify({'message': 'Success creating new user !'}), 200
    # return jsonify({'message': 'Error !'}), 404


@user_blueprint.route('/', methods=['GET'])
def get_users():
    return jsonify(service.get_all())


@user_blueprint.route('/<string:username>', methods=['GET'])
def get_user():
    req_args = request.view_args
    if 'username' in req_args: 
        username =  req_args['username']
    else:
        return jsonify({'message': 'Missing required request argument'}), 400

    if not service.check_user(username):
        return jsonify({'message': 'The username you entered does not exist'}), 400
    
    


@user_blueprint.route('/<string:username>', methods=['PATCH'])
def update_user(username: str):
    pass


@user_blueprint.route('/<string:username>', methods=['DELETE'])
def delete_user(username: str):
    pass


@user_blueprint.route('/', methods=['DELETE'])
def delete_users():
    pass

