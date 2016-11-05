import json
import os

from census import Census
from us import states

API_KEY = '3b91f1bb529e6b3b1c06733fbfbf2806d47b70ce'

population = 'B01003_001E'

census = Census(API_KEY)

filedir = os.path.dirname(os.path.realpath(__file__))
with open(filedir + '/data/de_census_boundaries.json') as fh:
    de_boundries = json.load(fh)

tract_geometries = dict([
    (feature['properties']['TRACTCE'], feature['geometry'])
    for feature in de_boundries['features']
])


def get_de_tract_pop(state=states.DE.fips):
    data = census.acs5.get(
        population,
        geo={'for': 'tract:*', 'in': 'state:{}'.format(state)}
    )

    for datum in data:
        datum['population'] = datum[population]
        del datum[population]

    features = [
        {
            "type": "Feature",
            'properties': datum,
            'geometry':  tract_geometries.get(datum['tract'])
        }
        for datum in data
    ]

    return features
