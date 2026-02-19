from os import getenv

class Config:
    MONGO_URI = getenv("MONGO_URI")
    SECRET_KEY = getenv("SECRET_KEY")