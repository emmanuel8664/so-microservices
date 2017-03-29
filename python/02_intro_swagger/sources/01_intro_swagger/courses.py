from flask import Flask, jsonify, request
from flasgger import Swagger
app = Flask(__name__)

Swagger(app)

@app.route('/courses', methods=['POST'])
def my_awesome_endpoint():
	"""
	This endpoint creates a course
	---
	tags:
	  -  create_course
	responses:
	  parameters:
	    - name: course
	      in: formData
	      description: course name
	      required: true
	      type: string
	  200:
	    description: course created
	    schema:
	      id: return_test
	      properties:
	        data:
	          type: object
	          properties:
	            course:
	              type: string
	              description: course name
	              default: 'operating systems'
	        status:
	          type: string
	          description: created or fail
	          default: 'created'
	"""
	data = request.json
	return jsonify(data=data, info={"status": "created"})

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000,debug='True')