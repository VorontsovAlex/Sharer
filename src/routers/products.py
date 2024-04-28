import os

import redis
from redis import Redis

from fastapi import APIRouter, Depends, Query, HTTPException, Path
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import FastAPI, File, UploadFile
import redis

from src.auth import JWTBearer
from src.database.products import ProductDatabaseService
from src.utils.helpers import get_db
from src.validators.products import ProductCreate, ProductUpdate
from src.models.models import ProductImages
from src.settings import image_vectorizer, text_vectorizer
from redis.commands.search.query import Query as RedisQuery


router = APIRouter()
product_db_service = ProductDatabaseService()



@router.get("/products/search/")
async def search_products123(
    db: Session = Depends(get_db),
    uploaded_file: UploadFile = File(...)
):
    conn = redis.Redis()

    conn = Redis(port=6379)
    contents = await uploaded_file.read()
    queries = image_vectorizer.vectorize(contents)

    query = (
        RedisQuery('(*)=>[KNN 3 @image_vector $query_vector AS vector_score]')
        # .sort_by('vector_score')
        .return_fields('vector_score', 'title', 'price', 'img', 'category')
        .dialect(2)
    )


    print(conn.ft("idx:product_vss").search(query, {
        'query_vector': queries.tobytes()
    }).docs)

    response = conn.json().get('product:0002541')
    # image_ids = response['ids']

    return JSONResponse(
        {
            'image_ids': []
        }
    )


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


@router.get("/products/{product_id}/")
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
    dependencies = Depends(JWTBearer())
):
    user = product_db_service.get_object(db, product_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/products/{product_id}/")
def update_product(
    product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db), dependencies=Depends(JWTBearer())
):
    existing_product = product_db_service.get_object(db, product_id)

    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = product_db_service.update_object(db, existing_product, product_update)

    return updated_product


@router.post("/products/{product_id}/image_upload/")
async def create_upload_file(
    db: Session = Depends(get_db),
    uploaded_file: UploadFile = File(...),
    product_id: int = Path()
):
    file_location = os.path.join(os.getcwd(), 'src/models/source/images/', uploaded_file.filename)

    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    product_db_service.save_product_image(
        db, product_id=product_id, filename=uploaded_file.filename, filelocation=file_location
    )
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}


@router.get("/products/{product_id}/images/")
async def get_files_by_producct(
    db: Session = Depends(get_db),
    product_id: int = Path()
):
    files = db.query(ProductImages).filter(ProductImages.id == product_id).all()

    if not files:
        raise HTTPException(status_code=404, detail="File not found")

    return [
        {"filename": file.filename, "file_path": file.file_path}
        for file in files
    ]



@router.get("/products/search/text")
async def search_products_text(
    db: Session = Depends(get_db),
    text_search: str = Query()
):
    conn = redis.Redis()
    queries = text_vectorizer.vectorize(text_search)

    query = (
        RedisQuery('(*)=>[KNN 3 @text_vector $query_vector AS vector_score]')
        .sort_by('vector_score')
        .return_fields('vector_score', 'title', 'price', 'img', 'category')
        .dialect(2)
    )
    print(conn.ft("idx:product_vss").search(query, {
        'query_vector': queries.tobytes()
    }).docs)

    return JSONResponse(
        {
            'image_ids': []
        }
    )


