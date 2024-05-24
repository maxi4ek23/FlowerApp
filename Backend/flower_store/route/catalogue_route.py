from flask import Blueprint, jsonify, request, Response
from flower_store.controller.catalogue_controller import CatalogueController

catalogue_bp = Blueprint('catalogue', __name__, url_prefix='/catalogue')
catalogue_controller = CatalogueController()


@catalogue_bp.post('')
def create_catalogue() -> Response:
    data = request.get_json()
    catalogue = catalogue_controller.create_catalogue(data)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.get('/<int:id>')
def get_catalogue(id: int) -> Response:
    catalogue = catalogue_controller.get_catalogue(id)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.get('')
def get_all_catalogues() -> Response:
    catalogues = catalogue_controller.get_all_catalogues()
    return jsonify([catalogue.put_into_dto() for catalogue in catalogues])


@catalogue_bp.put('/<int:id>')
def update_catalogue(id: int) -> Response:
    data = request.get_json()
    catalogue = catalogue_controller.update_catalogue(id, data)
    return jsonify(catalogue.put_into_dto())


@catalogue_bp.delete('/<int:id>')
def delete_catalogue(id: int) -> Response:
    catalogue_controller.delete_catalogue(id)
    return '', 204
