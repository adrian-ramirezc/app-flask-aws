from urllib import request
from flask import Flask, jsonify 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/name=<name>')
def return_name(name: str):
    return f'Hello {name}, welcome'

@app.route('/age=<age>')
def return_age(age: int):
    return f"You are {age} years old"


if __name__ == "__main__":
    app.run(debug=True)