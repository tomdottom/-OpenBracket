from flask import Blueprint, render_template

api = Blueprint('api', __name__)


@api.route('/')
def query():
    # return render_template('index.html')
    return "foo"
