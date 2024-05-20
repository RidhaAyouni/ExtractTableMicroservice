import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://user:password@localhost:5432/database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
