from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from src.database.users import UserDatabaseService
from src.settings import settings
from src.utils.helpers import get_db
from src.validators.users import UserCreate, UserUpdate

router = APIRouter()
user_db_service = UserDatabaseService()


@router.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = user_db_service.get_all(db)
    return users


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_db_service.get_object(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users/")
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user = user_db_service.save_object(db, user_create)
    return user


@router.put("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    existing_user = user_db_service.get_object(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = user_db_service.update_object(db, existing_user, user_update)
    return updated_user


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_db_service.get_object(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
