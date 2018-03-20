from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import DB_URL
app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL # 'postgresql://rjbrjpnryxbqmm:4d6ab507c820963240aa2cc4ab358dfc879b2961e7c82dc6aa9bb5a3286dc1a2@ec2-23-23-222-184.compute-1.amazonaws.com:5432/df1glh082k0rh'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
