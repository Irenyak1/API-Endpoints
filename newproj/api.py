from flask import Flask, request,jsonify, flash, redirect,session

app = Flask(__name__)

users = [
    {
        "name": "Moses Tete",
        "username": "wango",
        "email": "galiwango@gmail.com",
        "password": "kabulasoke1",
        "confirmation": "kabulasoke1"

    },
    {
        "name": "Samuel Bagonza",
        "username": "samex",
        "email": "teziita@gmail.com",
        "password": "goodislove",
        "confirmation": "goodislove"

    },
    {
        "name": "Daniel Stevens",
        "username": "bravo",
        "email": "semusu@gmail.com",
        "password": "yesuamala",
        "confirmation": "yesuamala"

    },
    {
        "name": "Jamie Jones",
        "username": "sampthon",
        "email": "sampthon@gmail.com",
        "password": "kamukama2",
        "confirmation": "kamukama2"

    },
    {
        "name": "Talmon Sidie",
        "username": "telolan",
        "email": "jjaviira@gmail.com",
        "password": "trumpet3",
        "confirmation": "trumpet3"

    }
]

@app.route('/', methods=['GET'])
def index():
    return 'index.html'


if __name__ == '__main__':
     app.run(debug=True)
