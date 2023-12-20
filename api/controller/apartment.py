from flask import Blueprint, request, jsonify
from service.apartment import ApartmentService
from service.authentification import AuthentificationService
from model.apartment import Apartment


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
    
    req_data = request.get_json()
    apartment = Apartment(None, req_data['username'], req_data['area'], req_data['max_people'], req_data['address'], req_data['availability'], None)  
    if not service.check_values(apartment):
        return jsonify({'message': 'The type of fields entered is not respected'}), 400
    print(service.create(apartment))
    return jsonify({'message': 'Success creating new apartment !'}), 200
    # return jsonify({'message': 'Error !'}), 404



@apartment_blueprint.route('/', methods=['GET'])
def get_apartments():
    return jsonify(service.get_all())


@apartment_blueprint.route('/<int:apartment_id>', methods=['GET'])
def get_apartment_id(apartment_id: int):
    apartment = service.get(apartment_id)
    if apartment:
        req_data = request.get_json()
        apartment_list_id = Apartment(None, req_data['username'], req_data['area'], req_data['max_people'], req_data['address'], req_data['availability'], None)
        service.get_all(apartment_list_id)
        return jsonify({'apartments': apartment_list_id})
    else:
        return jsonify({'message': 'Apartment not found'}), 404


@apartment_blueprint.route('/<string:username>', methods=['GET'])
def get_apartment_username():
    req_args = request.view_args
    if 'username' in req_args: 
        username =  req_args['username']
    else:
        return jsonify({'message': 'Missing required request argument'}), 400

    if not service.get_by_username(username):
        return jsonify({'message': 'The username you entered does not exist'}), 400
    else:
        return jsonify({'message': f'The desired user is: {username}'}), 200


@apartment_blueprint.route('/<int:apartment_id>', methods=['PATCH'])
def update_apartment(apartment_id: int):
    req_data = request.get_json()
    apartment = Apartment(None, req_data['username'], req_data['area'], req_data['max_people'], req_data['address'], req_data['availability'], None)
    service.update(apartment)
    return jsonify({'message': f'Successfully updated apartment: {apartment_id}'}), 200


@apartment_blueprint.route('/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id: int):
    apartment = service.get(apartment_id)
    if apartment:
        service.delete(apartment)
        return jsonify({'message': f'Successfully deleted apartment: {apartment_id}'}), 200
    else:
        return jsonify({'message': 'Apartment not found'}), 404


@apartment_blueprint.route('/', methods=['DELETE'])
def delete_apartments():
    service.delete_all()
    return jsonify({'message': 'All apartments deleted successfully'}), 200
