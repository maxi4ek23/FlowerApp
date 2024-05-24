from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flower_store.controller import bouquet_controller
from flower_store.model.flower import Flower

bouquet_bp = Blueprint('bouquet', __name__, url_prefix='/bouquet')
bouquet_controller_instance = bouquet_controller.BouquetController()


@bouquet_bp.post('')
def create_bouquet():
    data = request.get_json()
    eventType = data.get('eventType')
    price = data.get('price')
    packing = data.get('packing')
    catalogue = data.get('catalogue')
    flowers_data = data.get('flowers', [])
    flowers = []
    for flower_data in flowers_data:
        flower = Flower(
            name=flower_data.get('name'),
            color=flower_data.get('color'),
            price=flower_data.get('price')
        )
        flowers.append(flower)

    bouquet = bouquet_controller_instance.create_bouquet(eventType, price, flowers, packing, catalogue)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.CREATED)


@bouquet_bp.get('/<int:id>')
def get_bouquet(id: int) -> Response:
    bouquet = bouquet_controller_instance.get_bouquet(id)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.OK)


@bouquet_bp.get('')
def get_all_bouquets() -> Response:
    bouquets = bouquet_controller_instance.get_all_bouquets()
    bouquets_dto = [bouquet.put_into_dto() for bouquet in bouquets]
    return make_response(jsonify(bouquets_dto), HTTPStatus.OK)


@bouquet_bp.put('/<int:id>')
def update_bouquet(id: int) -> Response:
    data = request.get_json()
    eventType = data.get('eventType')
    price = data.get('price')
    packing = data.get('packing')
    catalogue = data.get('catalogue')
    flowers_data = data.get('flowers', [])
    flowers = []
    for flower_data in flowers_data:
        flower = Flower(
            name=flower_data.get('name'),
            color=flower_data.get('color'),
            price=flower_data.get('price')
        )
        flowers.append(flower)
    bouquet = bouquet_controller_instance.update_bouquet(id, eventType, price, flowers, packing, catalogue)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.OK)


@bouquet_bp.delete('/<int:id>')
def delete_bouquet(id: int) -> Response:
    bouquet_controller_instance.delete_bouquet(id)
    return make_response('', HTTPStatus.NO_CONTENT)
