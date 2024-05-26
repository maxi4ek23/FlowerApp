from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flower_store.controller import bouquet_controller
from flower_store.model.flower import Flower
from flask_cors import cross_origin

bouquet_bp = Blueprint('bouquet', __name__, url_prefix='/bouquet')



@bouquet_bp.post('')
@cross_origin()
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

    bouquet = bouquet_controller.create_bouquet(eventType, price, flowers, packing, catalogue)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.CREATED)


@bouquet_bp.get('/<int:id>')
@cross_origin()
def get_bouquet(id: int) -> Response:
    bouquet = bouquet_controller.get_bouquet(id)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.OK)


@bouquet_bp.get('event_type/<string:event_type>')
@cross_origin()
def get_bouquet_by_event(event_type: str) -> Response:
    bouquet = bouquet_controller.get_by_event(event_type)
    return make_response(jsonify(bouquet), HTTPStatus.OK)



@bouquet_bp.get('')
@cross_origin()
def get_all_bouquets() -> Response:
    bouquets = bouquet_controller.get_all_bouquets()
    bouquets_dto = [bouquet.put_into_dto() for bouquet in bouquets]
    return make_response(jsonify(bouquets_dto), HTTPStatus.OK)


@bouquet_bp.put('/<int:id>')
@cross_origin()
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
    bouquet = bouquet_controller.update_bouquet(id, eventType, price, flowers, packing, catalogue)
    return make_response(jsonify(bouquet.put_into_dto()), HTTPStatus.OK)


@bouquet_bp.delete('/<int:id>')
@cross_origin()
def delete_bouquet(id: int) -> Response:
    bouquet_controller.delete_bouquet(id)
    return make_response('', HTTPStatus.NO_CONTENT)
