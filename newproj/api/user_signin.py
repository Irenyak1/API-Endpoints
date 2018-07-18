from flask import Flask, jsonify, request
from api import app
from api import dummy_data


@app.route('/UI/signin_user', methods=['GET'])
def signin():
    return 'signin_user.html'

@app.route('/auth/signin_user', methods=['POST'])
def signin_user():
    # getting user signin data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'message': 'Please fill all fields'}), 400

    username = str(user_data.get('username')).strip()
    password = user_data.get('password')
    
    # validate user signin data
    if not username:
        return jsonify({'message': 'Username is required'}), 400
    
    if not password:
        return jsonify({'message': 'Password is required'}), 400
    
    return jsonify({ 'message': f'Hi {username} you are successfully logged in'}), 201

