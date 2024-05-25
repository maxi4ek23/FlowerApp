from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_cors import cross_origin

from flower_store.controller import order_controller

order_bp = Blueprint('order', __name__, url_prefix='/order')


@order_bp.post('')
@cross_origin()
def create_order() -> Response:
    data = request.get_json()
    order = order_controller.create_order(data)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.get('/<int:id>')
@cross_origin()
def get_order(id: int) -> Response:
    order = order_controller.get_order(id)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)


@order_bp.get('')
@cross_origin()
def get_all_orders() -> Response:
    orders = order_controller.get_all_orders()
    orders_dto = [order.put_into_dto() for order in orders]
    return make_response(jsonify(orders_dto), HTTPStatus.OK)


@order_bp.put('/<int:id>')
@cross_origin()
def update_order(id: int) -> Response:
    data = request.get_json()
    order = order_controller.update_order(id, data)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)


@order_bp.delete('/<int:id>')
@cross_origin()
def delete_order(id: int) -> Response:
    order_controller.delete_order(id)
    return make_response('', HTTPStatus.NO_CONTENT)
