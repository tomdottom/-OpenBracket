# app.py or app/__init__.py
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from views.api import api_bp
import views.api
import models
#import manage

from config import *

app = Flask(__name__)

# https://medium.com/building-socratic/the-one-weird-trick-that-cut-our-flask-page-load-time-by-70-87145335f679
app.jinja_env.cache = {}

config = os.getenv('CONFIG_OBJECT', 'LocalConfig')
#print 'loading config:', config
app.config.from_object(eval(config))

db = SQLAlchemy(app)

views.api.db = db
#models.init(db)
#manage.db = db
models.db = db

app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def index():
    return render_template('index.html')


available_data_endpoints = {
    'age': ('age', 'Average Age'),
    'commute-time': ('commute_time', 'Commute Time'),
    'employment': ('employment_employed', 'Employeed'),
}


@app.route('/census/<string:data_type>')
def census_data(data_type):
    category, description = available_data_endpoints[data_type]
    return render_template(
        'census_heatmap.html',
        category=category,
        description=description)
