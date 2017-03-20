from flask import Flask, jsonify, request
from flasgger import Swagger
app = Flask(__name__)

Swagger(app)

@app.route("/greeting", methods=['GET'])
def hello():
    """
    A hello world API
    This endpoint does nothing
    Only returns "Hello World"
    ---
    tags:
      - helloworldapi
    responses:
      200:
        description: A single user item
        schema:
          id: return_test
          properties:
            result:
              type: string
              description: The test
              default: 'test'
    """
    return jsonify({"result": "Hello World"})

if __name__ == "__main__":
      app.run(host='0.0.0.0',port=5000,debug='True')

