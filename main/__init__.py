from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from main.config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models
from main.routes_file import *