from flask import Flask, jsonify, request
from api import app
from api import dummy_data
from .models import Request, requests, User, users


@app.route('/signin_user', methods=['GET'])
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

@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200


@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('id') == user_id:
            return jsonify({'user': each_user})

    return jsonify({'error': 'User Not Found'}), 404
