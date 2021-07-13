import os

class Config:
    SECRET_KEY = os.urandom(23)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///todoapp.sqlite'