from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from time import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3' # use relative filepath for sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app) # initialize SQLAlchemy

# Import routes after initializing db to avoid circular imports
from routes import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # create database tables if they don't exist
    app.run(debug=True)
