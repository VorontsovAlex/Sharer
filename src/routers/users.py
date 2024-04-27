from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.auth import signJWT, JWTBearer
from src.database.users import UserDatabaseService
from src.utils.helpers import get_db
from src.validators.users import UserCreate, UserUpdate, UserRegister

router = APIRouter()
user_db_service = UserDatabaseService()


@router.get("/users/")
def read_users(db: Session = Depends(get_db), dependencies=Depends(JWTBearer())):
    users = user_db_service.get_all(db)
    return users


@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())):
    user = user_db_service.get_object(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users/")
def create_user(user_create: UserCreate, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())):
    user = user_db_service.save_object(db, user_create)
    return user


@router.put("/users/{user_id}")
def update_user(
    user_id: int, user_update: UserUpdate, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())
):
    existing_user = user_db_service.get_object(db, user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = user_db_service.update_object(db, existing_user, user_update)
    return updated_user


class UserLogin(BaseModel):
    email: str
    password: str


# Route for user registration
@router.post("/users/register/")
async def register_user(user: UserRegister, db: Session = Depends(get_db)):
    if user_db_service.get_object_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Username already registered")

    user_create = UserCreate(email=user.email, hashed_password=user.password)
    user_db_service.save_object(db, user_create)

    return signJWT(user.email)


@router.post("/users/login", tags=["user"])
async def user_login(user: UserLogin, db: Session = Depends(get_db)):
    if user_db_service.check_user_creds(db, user.email, user.password):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

# @router.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = user_db_service.get_object(db, user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(user)
#     db.commit()
#     return {"message": "User deleted successfully"}
