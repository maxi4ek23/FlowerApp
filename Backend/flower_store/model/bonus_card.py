from typing import Dict
from flower_store import db

from .i_dto import IDto

class BonusCard(db.Model, IDto):
    __tablename__ = "bonus_card"
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clientId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    bonus = db.Column(db.Float, default=0.0)
    free_delivery=db.Column(db.Boolean, default=False)

    def __init__(self, clientId: int, bonus: float):
        self.clientId = clientId
        self.bonus = bonus

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "clientId": self.clientId,
            "bonus": self.bonus,
            "free_delivery": self.free_delivery
        }
    
    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return BonusCard(
            clientId=dto_dict.get("clientId"),
            bonus=dto_dict.get("bonus")
        )