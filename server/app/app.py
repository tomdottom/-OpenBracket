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


@app.route('/age')
def age():
    return render_template('age.html')


@app.route('/commute-time')
def commute_time():
    return render_template('commute_time.html')


@app.route('/employment')
def employment():
	return render_template('employment_employed.html')

@app.route('/worker-flow')
def worker_flow():
    return render_template('worker_flow.html', name="foo")
