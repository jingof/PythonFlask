# export FLASK_APP=index.py
# export FLASK_ENV=development
# flask run
# curl http://127.0.0.1:5000/
from crypt import methods
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, T he World!"

incomes = [
  {'description':'salary','amount':5000}
]

@app.route("/incomes")
def get_incomes():
  return jsonify(incomes)

@app.route("/incomes", methods=["POST"])
def add_income():
  incomes.append(request.get_json())
  return '',204


"""
 add new income
curl -X POST -H "Content-Type: application/json" -d '{
  "description": "lottery",
  "amount": 1000.0
}' http://localhost:5000/incomes

# check if lottery was added
curl localhost:5000/incomes
"""
