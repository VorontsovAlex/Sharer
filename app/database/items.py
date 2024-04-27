from sqlalchemy.orm import Session
from src.models.models import Item


class ItemDatabaseService:
    def get_object(self, db: Session, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    def get_all(self, db: Session):
        """
        Retrieve all item objects from the database.
        """
        return db.query(Item).all()

    def save_object(self, db: Session, item: Item):
        """
        Save a new item object to the database.
        """
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def update_object(self, db: Session, item: Item):
        """
        Update an existing item object in the database.
        """
        db.merge(item)
        db.commit()
        return item
