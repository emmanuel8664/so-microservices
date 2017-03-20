from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/api/<string:username>')
def user_api(username):
    """
    User API
    This resource returns user information
    ---
    tags:
      - users
    parameters:
      - name: username
        in: path
        type: string
        required: true
    responses:
      200:
        description: A single user item
        schema:
          id: user_response
          properties:
            username:
              type: string
              description: The username
              default: some_username

    """
    return jsonify({'username': username})


if __name__ == "__main__":
      app.run(host='0.0.0.0',port=5000,debug='True')