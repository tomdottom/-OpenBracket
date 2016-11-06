from flask import Blueprint
from flask_restful import Resource, Api

import us_census.query
import us_census.api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

db = None

from .. import models


class Census(Resource):
    def get(self):
        return us_census.query.query()


class TractPopulations(Resource):
    def get(self):
        return us_census.api.get_de_tract_pop()


class CensusTractData(Resource):
    def get(self, data_type):
        return us_census.api.get_de_tract_data(data_type)


class CensusOriginDestinationEmployment(Resource):
    def get(self):

        tracts = db.session.query(models.CensusTractNonResidentWorker)

        obj_list = {
            t.geocode_tract: {
                'workers_in': t.workers_in,
                'workers_out': t.workers_out,
                'workers_diff': t.workers_diff
            }
            for t in tracts
        }

        return obj_list


api.add_resource(
    CensusOriginDestinationEmployment,
    '/census_origin_destination_employment/'
)
api.add_resource(TractPopulations, '/tract_populations/')
api.add_resource(Census, '/census/')
api.add_resource(CensusTractData, '/census/<string:data_type>')
