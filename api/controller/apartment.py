from flask import Blueprint, request, jsonify
from api.service.apartment import ApartmentService

apartment_blueprint = Blueprint('apartment', __name__)

service = ApartmentService

@apartment_blueprint.route('/', methods=['POST'])
def create_apartment():
    pass

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