from http import HTTPStatus

from flask import Blueprint, Response, make_response
from flask_cors import cross_origin

err_handler_bp = Blueprint('errors', __name__)


@err_handler_bp.app_errorhandler(HTTPStatus.NOT_FOUND)
@cross_origin()
def handle_404(error: int) -> Response:
    """
    Informs user that object not found in DB
    :param error: status code
    :return: Response object
    """
    return make_response("Object not found", HTTPStatus.NOT_FOUND)


@err_handler_bp.app_errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@cross_origin()
def handle_422(error: int) -> Response:
    """
    Informs user that input data is wrong or not full
    :param error: status code
    :return: Response object
    """
    return make_response("Input data is wrong or not full", HTTPStatus.UNPROCESSABLE_ENTITY)


@err_handler_bp.app_errorhandler(HTTPStatus.CONFLICT)
@cross_origin()
def handle_409(error: int) -> Response:
    """
    Informs user that input data is already exists in DB
    :param error: status code
    :return: Response object
    """
    return make_response("Such object is already exists in DB", HTTPStatus.CONFLICT)
