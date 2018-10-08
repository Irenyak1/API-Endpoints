from flask import Flask, request, jsonify
from api import app

@app.route('/', methods=['GET'])
def index():
    return 'index.html'

