from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from flask_cors import cross_origin

from flower_store.controller import flower_controller

flower_bp = Blueprint('flower', __name__, url_prefix='/flower')



@flower_bp.post('')
@cross_origin()
def create_flower():
    data = request.get_json()
    name = data.get('name')
    color = data.get('color')
    price = data.get('price')
    bouquet_id = data.get('bouquet_id')
    flower = flower_controller.create_flower(name, color, price)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.CREATED)


@flower_bp.get('/<int:id>')
@cross_origin()
def get_flower(id: int) -> Response:
    flower = flower_controller.get_flower(id)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.OK)


@flower_bp.get('')
@cross_origin()
def get_all_flowers() -> Response:
    flowers = flower_controller.get_all_flowers()
    flowers_dto = [flower.put_into_dto() for flower in flowers]
    return make_response(jsonify(flowers_dto), HTTPStatus.OK)

@flower_bp.get('name/<string:name>')
@cross_origin()
def get_flower_by_name(name: str) -> Response:
    flowers = flower_controller.get_flower_by_name(name)
    flowers_dto = [flower.put_into_dto() for flower in flowers]
    return jsonify(flowers_dto), 200



@flower_bp.put('/<int:id>')
@cross_origin()
def update_flower(id: int) -> Response:
    data = request.get_json()
    flower = flower_controller.update_flower(id, data)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.OK)


@flower_bp.delete('/<int:id>')
@cross_origin()
def delete_flower(id: int) -> Response:
    flower_controller.delete_flower(id)
    return make_response('', HTTPStatus.NO_CONTENT)
