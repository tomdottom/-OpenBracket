from flask import Blueprint
from flask_restful import Resource, Api

import us_census.query

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


class Census(Resource):
    def get(self):
        return us_census.query.query()

api.add_resource(Census, '/census/')
