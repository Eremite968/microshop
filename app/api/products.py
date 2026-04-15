from fastapi import Depends, APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductOut
from app.db.session import get_db
from app.services.product_service import ProductService


router = APIRouter(tags=["Products"])


@router.post("/",response_model=ProductOut,status_code=status.HTTP_201_CREATED)

def create_product(product: ProductCreate,db: Session = Depends(get_db)):
    try:
        return ProductService.create_product(db,product)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(exc))

@router.get("/",response_model=list[ProductOut])
def get_products(db:Session = Depends(get_db)):
    return ProductService.get_all_products(db)

@router.get("/{product_id}",response_model=ProductOut)
def get_product(product_id:int,db:Session = Depends(get_db)):
    product = ProductService.get_product(db,product_id)
    if not product:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Product not found")
    return product

@router.delete("/{product_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int,db:Session = Depends(get_db)):
    try:
      ProductService.delete_product(db,product_id)
      return None
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=str(exc))







