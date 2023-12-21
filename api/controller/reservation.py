from flask import Blueprint, request, jsonify
from service.reservation import ReservationService
from service.authentification import AuthentificationService
from service.user import UserService
from model.reservation import Reservation

reservation_blueprint = Blueprint('reservation', __name__)

user_service = UserService()
service = ReservationService()
auth = AuthentificationService()

@reservation_blueprint.route('/', methods=['POST'])
def create_reservation():
    authorization_header = request.headers.get('Authorization')
    if not authorization_header or not authorization_header.startswith('Basic '):
        return jsonify({'message': 'Authorization header missing or invalid'}), 401
    username, password = auth.extract_credentials(authorization_header)

    if username == "" or password == "":
        return jsonify({'message': 'Invalid credentials format'}), 401

    if not auth.authenticate_user(username, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    req_data = request.get_json()
    reservation = Reservation(None, req_data['start_date'], req_data['end_date'], req_data['price'], req_data['username'], None) 

    if not service.check_values(reservation):
        return jsonify({'message': 'The type of fields entered is not respected'}), 400    

    if not user_service.check_user(reservation.username):
        return jsonify({'message': 'User not found'}), 404

    service.create(reservation)
    return jsonify({'message': 'Success creating new reservation!'}), 200
    # return jsonify({'message': 'Error !'}), 404


@reservation_blueprint.route('/', methods=['GET'])
def get_reservations():
    return jsonify(service.get_all())


@reservation_blueprint.route('/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id: int):
    reservation = service.get(reservation_id)
    if reservation:
        return jsonify({'reservation': reservation})
    else:
        return jsonify({'message': 'Reservation not found'}), 404


@reservation_blueprint.route('/<int:reservation_id>', methods=['PATCH'])
def update_reservation(reservation_id: int):
    req_data = request.get_json()
    reservation = Reservation(None, req_data['apartment_id'], req_data['user_id'], req_data['start_date'], req_data['end_date'], None)
    service.update(reservation)
    return jsonify({'message': f'Successfully updated reservation: {reservation_id}'}), 200


@reservation_blueprint.route('/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id: int):
    reservation = service.get(reservation_id)
    if reservation:
        service.delete(reservation)
        return jsonify({'message': f'Successfully deleted reservation: {reservation_id}'}), 200
    else:
        return jsonify({'message': 'Reservation not found'}), 404


@reservation_blueprint.route('/', methods=['DELETE'])
def delete_reservations():
    service.delete_all()
    return jsonify({'message': 'All reservations deleted successfully'}), 200
