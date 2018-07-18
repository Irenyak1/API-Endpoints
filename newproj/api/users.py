from flask import Flask, jsonify, request
from api import app
from .models import Request, requests, User, users


@app.route('/users')
def get_all_users():
    return jsonify({'users': users}), 200


@app.route('/users/<int:user_id>')
def get_user(user_id):
    for each_user in users:
        if each_user.get('user_id') == user_id:
            return jsonify({'user': each_user})

    return jsonify({'error': 'User Not Found'}), 404
