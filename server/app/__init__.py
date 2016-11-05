# app.py or app/__init__.py
from flask import Flask, render_template
from views.api import api_bp

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def index():
    return render_template('index.html', name="foo")
