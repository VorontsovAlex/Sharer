from src.models.models import User

from sqlalchemy.orm import Session

from src.validators.users import UserCreate, UserUpdate


class UserDatabaseService:
    def get_object(self, db: Session, user_id: int):
        """
        Retrieve a user object by user_id from the database.
        """
        return db.query(User).filter(User.id == user_id).first()

    def get_all(self, db: Session):
        """
        Retrieve all user objects from the database.
        """
        return db.query(User).all()

    def save_object(self, db: Session, user_data: UserCreate):
        """
        Save a new user object to the database.
        """
        user = User(**dict(user_data))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_object(self, db: Session, user: User, user_data: UserUpdate):
        for field, value in user_data.dict().items():
            setattr(user, field, value)

        db.commit()
        db.refresh(user)
        return user
