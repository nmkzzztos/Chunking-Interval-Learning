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

class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'), nullable=False)

    def __init__(self, name):
        self.id = uuid4()
        self.name = name

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(50))
    back = db.Column(db.String(50))
    next_review = db.Column(db.Time)
    labels = db.relationship('Label', backref='card', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, front, back, labels):
        self.id = uuid4()
        self.front = front
        self.back = back
        self.next_review = time()
        self.labels = labels

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship('Card', backref='user', lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.cards = []

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/login', methods=['POST'])
def login():
    '''
    Logs a user in by adding their username to the session

    Returns:
        A JSON response containing a message indicating whether or not the user was logged in successfully
        >>> app.post('/login', json={
        ...     "username": "test",
        ...     "password": "test"
        ... })
        <Response streamed [200 OK]>
    '''
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(name=username).first()
    print(user.name)
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401
    return user, 200

@app.route('/register', methods=['POST'])
def register():
    '''
    Registers a user by adding them to the database

    Returns:
        A JSON response containing a message indicating whether or not the user was registered successfully
        >>> app.post('/register', json={
        ...     "username": "test",
        ...     "password": "test"
        ... })
        <Response streamed [201 CREATED]>
    '''
    username = request.json.get('username')
    password = request.json.get('password')

    user = User(username, password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/cards', methods=['GET'])
def get_cards():
    '''
    Gets all cards for a user

    Returns:
        A JSON response containing a list of all cards for the user
        >>> app.get('/cards')
        <Response streamed [200 OK]>
    '''
    username = request.json.get('username')
    user = User.query.filter_by(name=username).first()
    cards = Card.query.filter_by(user=user).all()
    return jsonify([card.front for card in cards]), 200

@app.route('/cards', methods=['POST'])
def add_card():
    '''
    Adds a card to the database

    Returns:
        A JSON response containing a message indicating whether or not the card was added successfully
        >>> app.post('/cards', json={
        ...     "front": "test",
        ...     "back": "test",
        ...     "labels": ["test"]
        ... })
        <Response streamed [201 CREATED]>
    '''
    front = request.json.get('front')
    back = request.json.get('back')
    labels = request.json.get('labels')
    username = request.json.get('username')
    user = User.query.filter_by(name=username).first()
    card = Card(front, back, labels)
    user.cards.append(card)
    db.session.add(card)
    db.session.commit()
    return jsonify({'message': 'Card created successfully'}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # create database tables if they don't exist
    app.run(debug=True)
