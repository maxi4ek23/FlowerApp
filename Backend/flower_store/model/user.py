from typing import Dict
from flower_store import db

from .i_dto import IDto

class User(db.Model, IDto):
    __tablename__ = "user"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45), nullable=False)
    email: str = db.Column(db.String(45), nullable=False)
    password: str = db.Column(db.String(45), nullable=False)
    is_admin: bool = db.Column(db.Boolean, nullable=False)
    bonus_card = db.relationship("BonusCard", backref="user")
    # bonus_card_id: int = db.Column(db.Integer, db.ForeignKey("bonus_card"))


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "is_admin": self.is_admin,
            "bonus_card": self.bonus_card[0].put_into_dto() if len(self.bonus_card) >= 1 else {}
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        obj = User(
            name = dto_dict.get("name"),
            email = dto_dict.get("email"),
            password = dto_dict.get("password"),
            is_admin = dto_dict.get("is_admin")
        )
        return obj