from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from flower_store.controller import packing_controller

packing_bp = Blueprint('packing', __name__, url_prefix='/packing')



@packing_bp.route('', methods=['POST'])
@cross_origin()
def create_packing():
    data = request.get_json()
    packing = packing_controller.create_packing(data)
    return jsonify(packing.put_into_dto()), 201


@packing_bp.route('/<int:id>', methods=['GET'])
@cross_origin()
def get_packing(id):
    packing = packing_controller.get_packing(id)
    return jsonify(packing.put_into_dto()), 200


@packing_bp.route('', methods=['GET'])
@cross_origin()
def get_all_packings():
    packings = packing_controller.get_all_packings()
    packings_dto = [packing.put_into_dto() for packing in packings]
    return jsonify(packings_dto), 200


@packing_bp.route('/<int:id>', methods=['PUT'])
@cross_origin()
def update_packing(id):
    data = request.get_json()
    packing = packing_controller.update_packing(id, data)
    return jsonify(packing.put_into_dto()), 200


@packing_bp.route('/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_packing(id):
    packing_controller.delete_packing(id)
    return '', 204
