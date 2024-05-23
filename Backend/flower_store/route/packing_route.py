from flask import Blueprint, jsonify, request
from flower_store.controller import packing_controller

packing_bp = Blueprint('packing', __name__, url_prefix='/packing')
flower_controller_instance = packing_controller.PackingController()


@packing_bp.route('', methods=['POST'])
def create_packing():
    data = request.get_json()
    packing = flower_controller_instance.create_packing(data)
    return jsonify(packing.put_into_dto()), 201


@packing_bp.route('/<int:id>', methods=['GET'])
def get_packing(id):
    packing = flower_controller_instance.get_packing(id)
    return jsonify(packing.put_into_dto()), 200


@packing_bp.route('', methods=['GET'])
def get_all_packings():
    packings = flower_controller_instance.get_all_packings()
    packings_dto = [packing.put_into_dto() for packing in packings]
    return jsonify(packings_dto), 200


@packing_bp.route('/<int:id>', methods=['PUT'])
def update_packing(id):
    data = request.get_json()
    packing = flower_controller_instance.update_packing(id, data)
    return jsonify(packing.put_into_dto()), 200


@packing_bp.route('/<int:id>', methods=['DELETE'])
def delete_packing(id):
    flower_controller_instance.delete_packing(id)
    return '', 204
