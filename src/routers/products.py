from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from src.auth import JWTBearer
from src.database.products import ProductDatabaseService
from src.utils.helpers import get_db
from src.validators.products import ProductCreate, ProductUpdate

router = APIRouter()
product_db_service = ProductDatabaseService()


@router.post("/products/")
def create_product(product_input: ProductCreate, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())):
    product = product_db_service.save_object(db, product_input)
    return product


@router.get("/products/")
def read_products(
    db: Session = Depends(get_db),
    category_id: int = Query(None),
    owner_id: int = Query(None),
    dependencies=Depends(JWTBearer())
):
    users = product_db_service.get_all(db, category_id, owner_id)
    return users


@router.get("/products/{product_id}")
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    dependencies = Depends(JWTBearer())
):
    user = product_db_service.get_object(db, product_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/products/{product_id}")
def update_user(
    product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), dependencies = Depends(JWTBearer())
):
    existing_product = product_db_service.get_object(db, product_id)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = product_db_service.update_object(db, existing_product, product_update)

    return updated_product
