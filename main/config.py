import os
from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath('.'), '.env'))

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SQLALCHEMY_ECHO = 0
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URI')
    IMGURL = environ.get('IMGURL')
    JWT_ALGORITHM = environ.get('JWT_ALGORITHM')