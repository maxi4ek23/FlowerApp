from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from flower_store.controller import category_controller
from flower_store.model import Category

category_bp = Blueprint('category', __name__, url_prefix='/category')

@category_bp.get('')
def get_all_categories() -> Response:
    """
    Gets all objects from table
    :return: Response object
    """
    return make_response(jsonify(category_controller.find_all()), HTTPStatus.OK)


@category_bp.post('')
def create_category() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()

    
    category = Category.create_from_dto(content)
    
   
    category_controller.create(category)
    return make_response(jsonify(category.put_into_dto()), HTTPStatus.CREATED)


# @category_bp.post('/login')
# def login_user() -> Response:
#     """
#     Gets all objects from table using Service layer.
#     :return: Response object
#     """
#     content = request.get_json()
#     # user = User.create_from_dto(**content)
#     # user_controller.create(user)
#     return make_response(jsonify(user_controller.login(**content)), HTTPStatus.CREATED)


@category_bp.get('/<int:category_id>')
def get_category(category_id: int) -> Response:
    """
    Gets category by ID.
    :return: Response object
    """
    return make_response(jsonify(category_controller.find_by_id(category_id)), HTTPStatus.OK)


@category_bp.put('/<int:category_id>')
def update_category(category_id: int) -> Response:
    """
    Updates category_id by ID.
    :return: Response object
    """
    content = request.get_json()
    category = Category.create_from_dto(content)
    category_controller.update(category_id, category)
    return make_response("Category updated", HTTPStatus.OK)


@category_bp.delete('/<int:category_id>')
def delete_category(category_id: int) -> Response:
    """
    Deletes category_id by ID.
    :return: Response object
    """
    category_controller.delete(category_id)
    return make_response("Category deleted", HTTPStatus.OK)