from flask import Flask, jsonify, request
from api import app
from .models import Request, requests, User, users


@app.route('/signup', methods=['GET'])
def sign_up():
    return 'signup.html'

@app.route('/auth/signup', methods=['POST'])
def signup_user():
    # getting user data
    user_data = request.get_json()

    if not user_data:
        return jsonify({'message': 'Please fill all the fields'}), 400

    name = user_data.get('name')
    username = user_data.get('username')
    email = user_data.get('email')
    password = user_data.get('password')
    confirmation = user_data.get('confirmation')

    # validate user data
    if not name:
        return jsonify({'message': 'name is required'}), 400

    if not username:
        return jsonify({'message': 'username is required'}), 400
  
    if not email:
        return jsonify({'message': 'email is required'}), 400
    
    if not password:
        return jsonify({'message': 'password is required'}), 400

    if not confirmation:
        return jsonify({'message': 'confirmation for password is required'}), 400
    
    user_data['id'] = len(users)
    # store your data to your database
    users.append(user_data)

    return jsonify({"message": f"user '{username}' has been successfully registered"}), 201

    
    



   