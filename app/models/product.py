<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Numeric
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
=======
from sqlalchemy import Column, Integer, String, Numeric
from app.db.session import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
>>>>>>> 9074d89 (Initial commit)
