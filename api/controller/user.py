from flask import Blueprint, request, jsonify
from api.service.user import UserService
from api.model.user import User
from api.service.authentification import AuthentificationService

user_blueprint = Blueprint('user', __name__)
auth = AuthentificationService
service = UserService

@user_blueprint.route('/', methods=['POST'])
def create_user():
    authorization_header = request.headers.get('Authorization')
    if not authorization_header or not authorization_header.startswith('Basic '):
        return jsonify({'message': 'Authorization header missing or invalid'}), 401
    username, password = auth.extract_credentials(authorization_header)
    
    if username is None or password is None:
        return jsonify({'message': 'Invalid credentials format'}), 401

    if not auth.authenticate_user(username, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    req_data = request.get_json()
    user = User(None, req_data['username'], req_data['first_name'], req_data['last_name'], req_data['password'], None)
    if service.create(user):
        return jsonify({'message': 'Success creating new user !'}), 200

## par sûr de celle la
@user_blueprint.route('/', methods=['GET'])
def get_users():
    req_data = request.get_json()
    user_list = User(None, req_data['username'], req_data['first_name'], req_data['last_name'], None)
    service.get_all(user_list)
    return jsonify({'users': user_list})


@user_blueprint.route('/<string:username>', methods=['GET'])
def get_user():
    req_args = request.view_args
    if 'username' in req_args: 
        username =  req_args['username']
    else:
        return jsonify({'message': 'Missing required request argument'}), 400

    if not service.check_user(username):
        return jsonify({'message': 'The username you entered does not exist'}), 400
    else:
        return jsonify({'message': f'The desired user is: {username}'}), 200


@user_blueprint.route('/<string:username>', methods=['PATCH'])
def update_user(username: str):
    req_data = request.get_json()
    user = User(None, req_data['username'], req_data['first_name'], req_data['last_name'], req_data['password'], None)
    user.username = username
    service.update(user)
    return jsonify({'message': f'Successfully updated user: {username}'}), 200


@user_blueprint.route('/<string:username>', methods=['DELETE'])
def delete_user(username: str):
    user = service.get(username)
    if user:
        service.delete(user)
        return jsonify({'message': f'Successfully deleted user: {username}'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@user_blueprint.route('/', methods=['DELETE'])
def delete_users():
    service.delete_all()
    return jsonify({'message': 'All users deleted successfully'}), 200
