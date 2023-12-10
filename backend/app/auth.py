from flask import request, jsonify
from werkzeug.security import generate_password_hash
from models import User
from app import app, db

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
    print(f'username: {username}, password: {password}')
    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid username or password'}), 401
    return jsonify({'message': 'Logged in successfully'}), 200

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
    hashed_password = generate_password_hash(password)

    user = User(username=username)
    user.set_password(hashed_password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201