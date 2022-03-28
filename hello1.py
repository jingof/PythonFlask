from flask import Flask
app = Flask(__name__)

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/

@app.route("/")
def hello_world():
    return "Hello, World!\n"