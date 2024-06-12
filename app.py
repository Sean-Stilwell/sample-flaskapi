# app.py
from flask import Flask, Blueprint
from flask_restx import Api, Resource

app = Flask(__name__)

# Create a blueprint
blueprint = Blueprint('api', __name__, url_prefix='/webapp-AHT')
api = Api(blueprint, doc='/')

ns = api.namespace('api', description='Sample API')

@ns.route('/')
class TestResource(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

# Register the blueprint with the app
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)