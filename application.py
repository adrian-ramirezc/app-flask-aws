from flask import Flask 
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hey there, how are you?'


if __name__ == "__main__":
    application.run(debug=True)