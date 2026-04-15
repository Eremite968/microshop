<<<<<<< HEAD
from fastapi import FastAPI


from app.api import products

app = FastAPI(title="Product Service")

app.include_router(products.router, prefix="/products",tags=["Products"])

@app.get("/health")
def health():
    return {"status": "ok"}
=======
from fastapi import FastAPI


from app.api import products

app = FastAPI(title="Product Service")

app.include_router(products.router, prefix="/products",tags=["Products"])

@app.get("/health")
def health():
    return {"status": "ok"}
>>>>>>> 9074d89 (Initial commit)
