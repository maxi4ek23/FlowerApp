from flask import Blueprint, jsonify, request, Response
from flask_cors import cross_origin
from flower_store.controller import catalogue_controller

catalogue_bp = Blueprint('catalogue', __name__, url_prefix='/catalogue')


@catalogue_bp.post('')
@cross_origin()
def create_catalogue() -> Response:
    data = request.get_json()
    catalogue = catalogue_controller.create_catalogue(data)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.get('/<int:id>')
@cross_origin()
def get_catalogue(id: int) -> Response:
    catalogue = catalogue_controller.get_catalogue(id)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.get('')
@cross_origin()
def get_all_catalogues() -> Response:
    catalogues = catalogue_controller.get_all_catalogues()
    return jsonify([catalogue.put_into_dto() for catalogue in catalogues])


@catalogue_bp.put('/<int:id>')
@cross_origin()
def update_catalogue(id: int) -> Response:
    data = request.get_json()
    catalogue = catalogue_controller.update_catalogue(id, data)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.delete('/<int:id>')
@cross_origin()
def delete_catalogue(id: int) -> Response:
    catalogue_controller.delete_catalogue(id)
    return '', 204
