from sqlalchemy.orm import Session
from src.models.models import Product, ProductImages
from src.validators.products import ProductCreate, ProductUpdate


class ProductDatabaseService:
    def get_object(self, db: Session, Product_id: int):
        return db.query(Product).filter(Product.id == Product_id).first()

    def get_all(self, db: Session, category_id: int, owner_id: int):
        query = db.query(Product)
        if category_id:
            query.filter(Product.category_id == category_id)
        if owner_id:
            query.filter(Product.owner_id == owner_id)

        return db.query(Product).all()

    def save_object(self, db: Session, product_data: ProductCreate):
        product = Product(**dict(product_data))
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update_object(self, db: Session, product: Product, product_data: ProductUpdate):
        for field, value in product_data.dict().items():
            setattr(product, field, value)

        db.commit()
        db.refresh(product)
        return product

    def save_product_image(self, db: Session, product_id, filename: str, filelocation: str):
        product_image = ProductImages(product_id=product_id, filename=filename, file_path=filelocation)
        db.add(product_image)
        db.commit()
        db.refresh(product_image)
        return product_image