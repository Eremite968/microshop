<<<<<<< HEAD
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/product_db"

settings = Settings()
=======
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/product_db"

settings = Settings()
>>>>>>> 9074d89 (Initial commit)
