from flask import Blueprint, request, jsonify
from service.apartment import ApartmentService
from service.authentification import AuthentificationService
from service.user import UserService
from model.apartment import Apartment


apartment_blueprint = Blueprint('apartment', __name__)

user_service = UserService()
service = ApartmentService()
auth = AuthentificationService()

@apartment_blueprint.route('/', methods=['POST'])
def create_apartment():
    # authorization_header = request.headers.get('Authorization')
    # if not authorization_header or not authorization_header.startswith('Basic '):
    #     return jsonify({'message': 'Authorization header missing or invalid'}), 401
    # username, password = auth.extract_credentials(authorization_header)

    # if username == "" or password == "":
    #     return jsonify({'message': 'Invalid credentials format'}), 401

    # if not auth.authenticate_admin(username, password):
    #     return jsonify({'message': 'Invalid username or password'}), 401
    
    req_data = request.get_json()
    if all(key in req_data for key in ("username", "area", "max_people", "address", "availability")):
        apartment = Apartment(None, req_data['area'], req_data['max_people'], req_data['address'], bool(req_data['availability']), req_data['username'])
    else:
        return jsonify({'message' : 'Arguments are not valid.', 'error': 'Bad Request'}), 400 
    
    if not service.check_values(apartment):
        return jsonify({'message': 'The type of fields entered is not respected'}), 400
    
    if not user_service.check_user(apartment.username):
        return jsonify({'message': 'The username you entered does not exist'}), 400

    service.create(apartment)
    return jsonify({'message': 'Success creating new apartment !'}), 200
  



@apartment_blueprint.route('/', methods=['GET'])
def get_apartments():
    return jsonify(service.get_all())


@apartment_blueprint.route('/<int:apartment_id>', methods=['GET'])
def get_apartment_id(apartment_id: int):
    apartment = service.get(apartment_id)
    if apartment:
        return jsonify(apartment)
    else:
        return jsonify({'message': 'Apartment not found'}), 404



@apartment_blueprint.route('/<int:apartment_id>', methods=['PATCH'])
def update_apartment(apartment_id: int):
    req_data = request.get_json()
    if all(key in req_data for key in ("username", "area", "max_people", "address", "availability")):
        apartment = Apartment(apartment_id, req_data['area'], req_data['max_people'], req_data['address'], bool(req_data['availability']), req_data['username'])
    else:
        return jsonify({'message' : 'Arguments are not valid.', 'error': 'Bad Request'}), 400 
    
    if not service.check_values(apartment):
        return jsonify({'message': 'The type of fields entered is not respected'}), 400
    
    if not service.get(apartment_id):
       return jsonify({'message': 'Apartment not found'}), 404
    
    if not user_service.check_user(apartment.username):
        return jsonify({'message': 'The username you entered does not exist'}), 400

    service.update(apartment)
    return jsonify({'message': f'Successfully updated apartment: {apartment_id}'}), 200


@apartment_blueprint.route('/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id: int):
    if not service.get(apartment_id):
       return jsonify({'message': 'Apartment not found'}), 404

    service.delete(apartment_id)
    return jsonify({'message': f'Successfully deleted apartment: {apartment_id}'}), 200


@apartment_blueprint.route('/', methods=['DELETE'])
def delete_apartments():
    service.delete_all()
    return jsonify({'message': 'All apartments deleted successfully'}), 200
