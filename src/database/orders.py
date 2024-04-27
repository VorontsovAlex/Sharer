from src.models.models import Order, User

from sqlalchemy.orm import Session

from src.validators.users import UserCreate, UserUpdate


class UserDatabaseService:
    def get_object(self, db: Session, order_id: int):
        """
        Retrieve a user object by user_id from the database.
        """
        return db.query(Order).filter(Order.id == order_id).first()
