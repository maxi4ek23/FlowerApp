from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from flower_store.controller import goods_controller
from flower_store.model import Goods

goods_bp = Blueprint('goods', __name__, url_prefix='/goods')

@goods_bp.get('')
def get_all_goods() -> Response:
    """
    Gets all objects from table
    :return: Response object
    """
    return make_response(jsonify(goods_controller.find_all()), HTTPStatus.OK)


@goods_bp.post('')
def create_goods() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()

   
    goods = Goods.create_from_dto(content)
    

    goods_controller.create(goods)
    return make_response(jsonify(goods.put_into_dto()), HTTPStatus.CREATED)


@goods_bp.post('/login')
def login_goods() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    # user = User.create_from_dto(**content)
    # user_controller.create(user)
    return make_response(jsonify(goods_controller.login(**content)), HTTPStatus.CREATED)


@goods_bp.get('/<int:goods_id>')
def get_goods(goods_id: int) -> Response:
    """
    Gets goods by ID.
    :return: Response object
    """
    return make_response(jsonify(goods_controller.find_by_id(goods_id)), HTTPStatus.OK)


@goods_bp.put('/<int:goods_id>')
def update_goods(goods_id: int) -> Response:
    """
    Updates goods_id by ID.
    :return: Response object
    """
    content = request.get_json()
    goods = Goods.create_from_dto(content)
    goods_controller.update(goods_id, goods)
    return make_response("Goods updated", HTTPStatus.OK)


@goods_bp.delete('/<int:goods_id>')
def delete_goods(goods_id: int) -> Response:
    """
    Deletes goods_id by ID.
    :return: Response object
    """
    goods_controller.delete(goods_id)
    return make_response("Goods deleted", HTTPStatus.OK)