from flask import abort
from http import HTTPStatus

from .general_controller import GeneralController
from flower_store.model import Goods

class GoodsController(GeneralController):
    _model_type = Goods

    
