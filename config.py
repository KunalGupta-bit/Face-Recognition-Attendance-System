from os import getenv
from datetime import timedelta

class Config:
    MONGO_URI = getenv("MONGO_URI")
    SECRET_KEY = getenv("SECRET_KEY")
    JWT_SECRET_KEY = getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)