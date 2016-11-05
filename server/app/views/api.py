from flask import Blueprint
from flask_restful import Resource, Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class SampleData(Resource):
    def get(self):
        return [39.74, -75.545, 15]

api.add_resource(SampleData, '/')
