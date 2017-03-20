from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)

Swagger(app)

@app.route("/greeting", methods=['GET'])
@swag_from('index.yml')
def hello_get():
    return jsonify({"result": "Hello get"})

@app.route("/greeting", methods=['POST'])
@swag_from('index.yml')
def hello_post():
    return jsonify({"result": "Hello post"})

@app.route("/goodbye", methods=['POST'])
@swag_from('index.yml')
def bye_post():
    return jsonify({"result": "Bye post"})

if __name__ == "__main__":
      app.run(host='0.0.0.0',port=5000,debug='True')