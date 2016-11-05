# app.py or app/__init__.py
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from views.api import api_bp

from config import *

app = Flask(__name__)

# https://medium.com/building-socratic/the-one-weird-trick-that-cut-our-flask-page-load-time-by-70-87145335f679
app.jinja_env.cache = {}

config = os.getenv('CONFIG_OBJECT', 'LocalConfig')
#print 'loading config:', config
app.config.from_object(eval(config))

db = SQLAlchemy(app)

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('index.html', name="foo")


@app.route('/test')
def test():
    return render_template('index.html', name="foo")

