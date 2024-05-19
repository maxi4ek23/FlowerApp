from typing import Dict
from flower_store import db

from .i_dto import IDto

class Category(db.Model, IDto):
    __tablename__ = "category"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45), nullable=False)


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        obj = Category(
            name = dto_dict.get("name"),
          
        )
        return obj