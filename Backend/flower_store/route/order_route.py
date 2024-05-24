from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from flower_store.controller import order_controller

order_controller_instance = order_controller.OrderController()
order_bp = Blueprint('order', __name__, url_prefix='/order')


@order_bp.post('')
def create_order() -> Response:
    data = request.get_json()
    order = order_controller_instance.create_order(data)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.CREATED)


@order_bp.get('/<int:id>')
def get_order(id: int) -> Response:
    order = order_controller_instance.get_order(id)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)


@order_bp.get('')
def get_all_orders() -> Response:
    orders = order_controller_instance.get_all_orders()
    orders_dto = [order.put_into_dto() for order in orders]
    return make_response(jsonify(orders_dto), HTTPStatus.OK)


@order_bp.put('/<int:id>')
def update_order(id: int) -> Response:
    data = request.get_json()
    order = order_controller_instance.update_order(id, data)
    return make_response(jsonify(order.put_into_dto()), HTTPStatus.OK)


@order_bp.delete('/<int:id>')
def delete_order(id: int) -> Response:
    order_controller_instance.delete_order(id)
    return make_response('', HTTPStatus.NO_CONTENT)
