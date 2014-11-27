from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #tells Flask to read and use the config.py file
db = SQLAlchemy(app) #db object, the database, created here 

from app import views, models