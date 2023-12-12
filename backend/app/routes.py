from flask import request, jsonify
from app import app, db
from models import User, Card, Label


@app.route("/login", methods=["POST"])
def login():
    """
    Logs a user in by adding their username to the session

    Returns:
        A JSON response containing a message indicating whether or not the user was logged in successfully
        >>> app.post('/login', json={
        ...     "username": "test",
        ...     "password": "test"
        ... })
        <Response streamed [200 OK]>
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = User.query.filter_by(name=username).first()
    if user is None or not user.check_password(password):
        return jsonify({"message": "Invalid username or password"}), 401
    return jsonify({"user": user.name}), 200


@app.route("/register", methods=["POST"])
def register():
    """
    Registers a user by adding them to the database

    Returns:
        A JSON response containing a message indicating whether or not the user was registered successfully
        >>> app.post('/register', json={
        ...     "username": "test",
        ...     "password": "test"
        ... })
        <Response streamed [201 CREATED]>
    """
    username = request.json.get("username")
    password = request.json.get("password")

    user = User(username, password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@app.route("/cards", methods=["GET"])
def get_cards():
    """
    Gets all cards for a user

    Returns:
        A JSON response containing a list of all cards for the user
        >>> app.get('/cards')
        <Response streamed [200 OK]>
    """
    username = request.json.get("username")
    user = User.query.filter_by(name=username).first()
    cards = Card.query.filter_by(user=user).all()
    return jsonify([card.front for card in cards]), 200


@app.route("/cards", methods=["POST"])
def add_card():
    """
    Adds a card to the database

    Returns:
        A JSON response containing a message indicating whether or not the card was added successfully
        >>> app.post('/cards', json={
        ...     "front": "test",
        ...     "back": "test",
        ...     "labels": ["test"]
        ... })
        <Response streamed [201 CREATED]>
    """
    front = request.json.get("front")
    back = request.json.get("back")
    username = request.json.get("username")

    user = User.query.filter_by(name=username).first()
    user_id = user.id

    card = Card(front, back, user_id)
    db.session.add(card)
    db.session.commit()

    return jsonify({"message": "Card created successfully"}), 201
