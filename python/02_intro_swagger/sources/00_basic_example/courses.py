from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/courses', methods=['POST'])
def create_user():
    data = request.json
    return jsonify(data=data, info={"status": "created"})

app.run()
