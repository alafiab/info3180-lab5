from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_URL
app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
