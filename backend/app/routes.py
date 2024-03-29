import os
import http.client

from flask import request, jsonify
from app import app, db
from models import User, Card


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
    cards = Card.query.filter_by(user=user).all()
    cards_to_response = {}
    for id, card in enumerate(cards):
        cards_to_response[id] = {
            "card_id": card.id,
            "front": card.front,
            "back": card.back,
            "labels": card.labels,
            "next_review": card.next_review,
            "repeat_count": card.repeat_count,
        }
    return jsonify({"user": user.name, "cards": cards_to_response}), 200


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

    if db.session.query(User.id).filter_by(name=username).scalar() is not None:
        return jsonify({"message": "User already exists"}), 409

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
        ...     "labels": ["test"],
        ...     "username": "test"
        ... })
        <Response streamed [201 CREATED]>
    """
    front = request.json.get("front")
    back = request.json.get("back")
    labels = request.json.get("labels")
    username = request.json.get("username")
    next_review = request.json.get("next_review")

    labels = "".join(labels)

    if not all([front, back, labels, username, next_review]):
        return jsonify({"message": "Missing data"}), 400

    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    card = Card(
        user_id=user.id, front=front, back=back, labels=labels, next_review=next_review
    )

    db.session.add(card)
    db.session.commit()

    return jsonify({"message": "Card created successfully"}), 201


@app.route("/cards", methods=["DELETE"])
def delete_card():
    """
    Deletes a card from the database

    Returns:
        A JSON response containing a message indicating whether or not the card was deleted successfully
        >>> app.put('/cards', json={
        ...     "front": "test",
        ...     "username": "test"
        ... })
        <Response streamed [200 OK]>
    """
    card_id = request.json.get("card_id")
    username = request.json.get("username")

    if not all([card_id, username]):
        return jsonify({"message": "Missing data"}), 400

    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    card = Card.query.filter_by(user_id=user.id, id=card_id).first()
    if not card:
        return jsonify({"message": "Card not found"}), 404

    db.session.delete(card)
    db.session.commit()

    return jsonify({"message": "Card deleted successfully"}), 200


@app.route("/cards", methods=["PUT"])
def updateCard():
    """
    Updates a card in the database

    Returns:
        A JSON response containing a message indicating whether or not the card was updated successfully
        >>> app.put('/cards', json={
        ...     "front": "test",
        ...     "username": "test"
        ... })
        <Response streamed [200 OK]>
    """
    card_id = request.json.get("card_id")
    username = request.json.get("username")
    next_review = request.json.get("next_review")
    repeat_count = request.json.get("repeat_count")

    if not all([card_id, username, next_review, repeat_count]):
        return jsonify({"message": "Missing data"}), 400

    user = User.query.filter_by(name=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    card = Card.query.filter_by(user_id=user.id, id=card_id).first()
    if not card:
        return jsonify({"message": "Card not found"}), 404

    card.next_review = next_review
    card.repeat_count = repeat_count
    db.session.commit()

    return jsonify({"message": "Card updated successfully"}), 200


@app.route("/translate", methods=["GET"])
def translate():
    """
    Translates text from one language to another

    Returns:
        A JSON response containing the translated text
        >>> app.get('/translate?text=test&langpair=en|es')
        <Response streamed [200 OK]>
    """
    text = request.args.get("text")
    langpair = request.args.get("langpair")

    if not text or not langpair:
        return jsonify({"message": "Missing text or langpair"}), 400

    conn = http.client.HTTPSConnection(
        "translated-mymemory---translation-memory.p.rapidapi.com"
    )

    headers = {
        "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "translated-mymemory---translation-memory.p.rapidapi.com",
    }

    try:
        conn.request(
            "GET",
            f"/get?langpair={langpair}&q={text}&mt=1&onlyprivate=0&de=a%40b.c",
            headers=headers,
        )
        res = conn.getresponse()
        data = res.read()
        return jsonify({"translation": data.decode("utf-8")}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500
