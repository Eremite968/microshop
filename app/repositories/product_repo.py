<<<<<<< HEAD
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductRepository:

    @staticmethod
    def create(db: Session, product: ProductCreate) -> Product:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def get_all(db: Session) -> list[Product]:
        return db.query(Product).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int) -> Product | None:
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def delete(db: Session, product: Product) -> None:
        db.delete(product)
        db.commit()
=======
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductRepository:

    @staticmethod
    def create(db: Session, product: ProductCreate) -> Product:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def get_all(db: Session) -> list[Product]:
        return db.query(Product).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int) -> Product | None:
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def delete(db: Session, product: Product) -> None:
        db.delete(product)
        db.commit()
>>>>>>> 9074d89 (Initial commit)
