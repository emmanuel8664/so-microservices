from flasgger.utils import swag_from, validate, ValidationError

@app.route('/api/<string:language>/', methods=['GET'])
@swag_from('index.yml')
def index(language):
    ...
    try:
        validate(data, 'awesome', 'index.yml', root=__file__)
    except ValidationError as e:
        return "Validation Error: %s" % e, 400
    ...