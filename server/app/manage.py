
import datetime

import csv

from flask_script import Manager

from app import app, db

from models import *

manager = Manager(app)

"""
Command line interface for OpenBracket

From root directory, call:

> python -m app.manage COMMAND

Such as:

> python -m app.manage test_print


"""


@manager.command
def test_print():
    """
    Call this function to make sure manage is working
    """
    print "Hello app! CLI works."






@manager.command
def store_census_origin_destination_employment():
    """

    TRUNCATE census_origin_destination_employment;

    TRUNCATE census_tract_non_resident_workers;

    INSERT INTO `census_tract_non_resident_workers` 
        SELECT null,  SUBSTRING(w_geocode, 1, 11), SUM(`S000`), 0, 0
            FROM census_origin_destination_employment GROUP BY SUBSTRING(w_geocode, 1, 11)


    UPDATE `census_tract_non_resident_workers` t
        SET t.workers_out = ( SELECT SUM(c.`S000`) FROM `census_origin_destination_employment` c 
            WHERE SUBSTRING(c.`h_geocode`, 1, 11)= t.`geocode_tract`);


    UPDATE `census_tract_non_resident_workers`
        SET workers_diff = workers_in - workers_out;



    """

    file_locations = ['/home/chris/projects/de_scrape/census/de_od_main_JT00_2014.csv', 
                      '/home/chris/projects/de_scrape/census/de_od_aux_JT00_2014.csv',
                      '/home/chris/projects/de_scrape/census/md_od_aux_JT00_2014.csv',
                      '/home/chris/projects/de_scrape/census/pa_od_aux_JT00_2014.csv',
                      '/home/chris/projects/de_scrape/census/nj_od_aux_JT00_2014.csv']                      

    for file_location in file_locations:

        print 'starting file:', file_location

        line = 0

        csvfile = open(file_location, 'r')

        csvreader = csv.reader(csvfile)

        row = next(csvreader)   # skip the first line

        fields = ['w_geocode', 'h_geocode', 'S000', 'SA01', 'SA02', 'SA03', 'SE01', 'SE02', 'SE03', 'SI01', 
            'SI02', 'SI03', 'createdate']

        for row in csvreader:

            line += 1

            row_values = dict(zip(fields, row))

            #if line < 10:
            #    print row
            #    print row_values

            census_data = CensusOriginDestinationEmployment(**row_values)

            db.session.add(census_data)        
                    
            if line % 1000 == 0:
                db.session.commit()                    

    db.session.commit()



