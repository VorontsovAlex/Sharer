from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.models.init_db import create_initial_data, drop_all_tables
from src.models.update_sequnce import update_sequence
from src.settings import settings
print(settings)

engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    products = relationship("Product", back_populates="owner")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    category_id = Column(Integer, ForeignKey("categories.id", ondelete='CASCADE'))
    price_per_hour = Column(DECIMAL)
    available_from = Column(Date, nullable=True)
    available_to = Column(Date, nullable=True)

    owner = relationship("User", back_populates="products")
    # category = relationship("Category", back_populates="products")


class ProductImages(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete='CASCADE'))
    filename = Column(String, index=True)
    file_path = Column(String)

    # product = relationship("Product", back_populates="images")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
    vendor_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))

    customer = relationship("User", foreign_keys=[customer_id])
    vendor = relationship("User", foreign_keys=[vendor_id])


if __name__ == "__main__":
    # Create the tables in the database
    drop_all_tables()
    Base.metadata.create_all(engine)
    create_initial_data()
    update_sequence()

# #
# # File storage functions
# def save_file(file: UploadFile) -> str:
#     with open(file.filename, "wb") as buffer:
#         buffer.write(file.file.read())
#     return file.filename
#
# def get_file_path(filename: str) -> str:
#     return filename  # Modify this function based on your file storage mechanism

