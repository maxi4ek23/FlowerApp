from flask import abort
from http import HTTPStatus

from .general_controller import GeneralController
from flower_store.model import BonusCard
from flower_store import db

class BonusCardController(GeneralController):
    def __init__(self):
        self._model_type = BonusCard

    def create_bonus_card(self, data):
        try:
            bonus_card = self._model_type.create_from_dto(data)
            self._session.add(bonus_card)
            self._session.commit()
            return bonus_card
        except Exception as e:
            db.session.rollback()
            raise e