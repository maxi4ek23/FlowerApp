from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_cors import cross_origin

from flower_store.controller import bonus_card_controller
from flower_store.model import bonus_card

bonus_card_bp = Blueprint('bonus_card', __name__, url_prefix='/bonus_card')

@bonus_card_bp.post('')
@cross_origin()
def create_bonus_card() -> Response:
    data = request.get_json()
    bonus_card = bonus_card_controller.create_bonus_card(data)
    return make_response(jsonify(bonus_card.put_into_dto()), HTTPStatus.CREATED)