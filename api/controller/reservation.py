from flask import Blueprint, request
from api.service.reservation import ReservationService

reservation_blueprint = Blueprint('reservation', __name__)

service = ReservationService

@reservation_blueprint.route('/', methods=['POST'])
def create_reservation():
    pass

@reservation_blueprint.route('/', methods=['GET'])
def get_reservations():
    pass

@reservation_blueprint.route('/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id: int):
    pass

@reservation_blueprint.route('/<int:reservation_id>', methods=['PATCH'])
def update_reservation(reservation_id: int):
    pass

@reservation_blueprint.route('/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id: int):
    pass

@reservation_blueprint.route('/', methods=['DELETE'])
def delete_reservations():
    pass