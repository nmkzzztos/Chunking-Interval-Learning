from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from time import time


class Label(db.Model):
    """
    A label for a card

    Attributes:
        id: A unique identifier for the label
        name: The name of the label
        card_id: The id of the card that the label belongs to
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    card_id = db.Column(db.Integer, db.ForeignKey("card.id"), nullable=False)

    def __init__(self, name):
        self.id = uuid4()
        self.name = name


class Card(db.Model):
    """
    A flashcard

    Attributes:
        id: A unique identifier for the card
        front: The front of the card
        back: The back of the card
        next_review: The time at which the card should be reviewed next
        labels: A list of labels for the card
        user_id: The id of the user that the card belongs to
    """

    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(50))
    back = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, front, back, user_id):
        self.front = front
        self.back = back
        self.user_id = user_id


class User(db.Model):
    """
    A user

    Attributes:
        id: A unique identifier for the user
        name: The name of the user
        password_hash: The hashed password of the user
        cards: A list of cards for the user
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    cards = db.relationship("Card", backref="user", lazy=True)

    def __init__(self, name, password):
        self.name = name
        self.password_hash = generate_password_hash(password)
        self.cards = []

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
