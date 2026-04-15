from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate
from app.repositories.product_repo import ProductRepository

class ProductService:
    @staticmethod
    def create_product(db:Session,product:ProductCreate):
        if product.price <= 0:
            raise ValueError("Product cannot be negative")
        return ProductRepository.create_product(db,product)
    @staticmethod
    def get_product(db:Session,product_id:int):
        return ProductRepository.get_by_id(db,product_id)
    @staticmethod
    def get_products(db:Session):
        return ProductRepository.get_all(db)
    @staticmethod
    def delete_product(db:Session,product_id:int):
        product = ProductRepository.get_by_id(db,product_id)
        if not product:
            raise ValueError("Not found")
        ProductRepository.delete(db,product)


