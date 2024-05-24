from typing import Dict
from flower_store import db

from .i_dto import IDto

class Goods(db.Model, IDto):
    __tablename__ = "goods"

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45), nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    description: str = db.Column(db.Text)
    image: str = db.Column(db.String(100))
    category_id: int = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
   

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "image": self.image,
            "category_id": self.category_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        obj = Goods(
            name = dto_dict.get("name"),
            price = dto_dict.get("price"),
            description = dto_dict.get("description"),
            image = dto_dict.get("image"),
            category_id = dto_dict.get("category_id")
        )
        return obj