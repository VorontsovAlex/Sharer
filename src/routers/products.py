from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile

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
def update_product(
    product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())
):
    existing_product = product_db_service.get_object(db, product_id)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = product_db_service.update_object(db, existing_product, product_update)

    return updated_product


@router.put("/products/{product_id}/image_upload")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"models/source/images/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}


# # API endpoints
# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     filename = save_file(file)
#     db = SessionLocal()
#     db_file = FileModel(filename=filename, file_path=get_file_path(filename))
#     db.add(db_file)
#     db.commit()
#     db.refresh(db_file)
#     return {"filename": filename, "file_path": db_file.file_path}
#
# @app.get("/files/", response_model=List[FileModel])
# async def get_files():
#     db = SessionLocal()
#     return db.query(FileModel).all()
#
# @app.get("/file/{file_id}/")
# async def get_file(file_id: int):
#     db = SessionLocal()
#     file = db.query(FileModel).filter(FileModel.id == file_id).first()
#     if not file:
#         raise HTTPException(status_code=404, detail="File not found")
#     return {"filename": file.filename, "file_path": file.file_path}
