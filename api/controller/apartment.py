from flask import Blueprint, request, jsonify
from service.apartment import ApartmentService
from service.authentification import AuthentificationService

apartment_blueprint = Blueprint('apartment', __name__)

service = ApartmentService()
auth = AuthentificationService()

@apartment_blueprint.route('/', methods=['POST'])
def create_apartment():
    authorization_header = request.headers.get('Authorization')
    if not authorization_header or not authorization_header.startswith('Basic '):
        return jsonify({'message': 'Authorization header missing or invalid'}), 401
    username, password = auth.extract_credentials(authorization_header)

    if username == "" or password == "":
        return jsonify({'message': 'Invalid credentials format'}), 401

    if not auth.authenticate_user(username, password):
        return jsonify({'message': 'Invalid username or password'}), 401



@apartment_blueprint.route('/', methods=['GET'])
def get_apartments():
    pass

@apartment_blueprint.route('/<int:apartment_id>', methods=['GET'])
def get_apartment(apartment_id: int):
    pass

@apartment_blueprint.route('/<int:apartment_id>', methods=['PATCH'])
def update_apartment(apartment_id: int):
    pass

@apartment_blueprint.route('/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id: int):
    pass

@apartment_blueprint.route('/', methods=['DELETE'])
def delete_apartments():
    pass