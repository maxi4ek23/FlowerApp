from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from flower_store.controller import flower_controller

flower_bp = Blueprint('flower', __name__, url_prefix='/flower')
flower_controller_instance = flower_controller.FlowerController()


@flower_bp.post('')
def create_flower():
    data = request.get_json()
    name = data.get('name')
    color = data.get('color')
    price = data.get('price')
    flower = flower_controller_instance.create_flower(name, color, price)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.CREATED)


@flower_bp.get('/<int:id>')
def get_flower(id: int) -> Response:
    flower = flower_controller_instance.get_flower(id)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.OK)


@flower_bp.get('')
def get_all_flowers() -> Response:
    flowers = flower_controller_instance.get_all_flowers()
    flowers_dto = [flower.put_into_dto() for flower in flowers]
    return make_response(jsonify(flowers_dto), HTTPStatus.OK)


@flower_bp.put('/<int:id>')
def update_flower(id: int) -> Response:
    data = request.get_json()
    flower = flower_controller_instance.update_flower(id, data)
    return make_response(jsonify(flower.put_into_dto()), HTTPStatus.OK)


@flower_bp.delete('/<int:id>')
def delete_flower(id: int) -> Response:
    flower_controller_instance.delete_flower(id)
    return make_response('', HTTPStatus.NO_CONTENT)
