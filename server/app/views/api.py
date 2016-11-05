from flask import Blueprint
from flask_restful import Resource, Api

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def CenusDatum(
    latitude, longditude, jobs_total,
    age_0_29, age_30_54, age_55_plus,
    monthly_wage_0_1250, monthly_wage_1251_3333, monthly_wage_3333_plus,
    goods_producing,
    trade_transportation_utilities,
    other_sectors,
    date
):

    return {
        "latitude": latitude,
        "longditude": longditude,
        "jobsTotal": jobs_total,
        "age0to29": age_0_29,
        "age30to54": age_30_54,
        "age55plus": age_55_plus,
        "monthlyWage0to1250": monthly_wage_0_1250,
        "monthlyWage1251to3333": monthly_wage_1251_3333,
        "monthlyWage3333plus": monthly_wage_3333_plus,
        "goodsProducing": goods_producing,
        "tradeTransportationUtilities": trade_transportation_utilities,
        "otherSectors": other_sectors,
        "date": date
    }


class FakeCensus(Resource):
    def get(self):
        return [
            CenusDatum(39.72, -75.545, 15, 6, 10, 14, 1, 1, 1, 1, 1, 1, "foo"),
            CenusDatum(39.74, -75.544, 15, 7, 5, 3, 1, 1, 1, 1, 1, 1, "foo")
        ]

api.add_resource(FakeCensus, '/census/')
