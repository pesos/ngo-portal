# Local project imports
from core import app
from core.models import User
import helpers as util

# Standard python imports
import json

# Third party imports
from flask import render_template, jsonify, request

# Application homepage
@app.route("/")
def index():
    return render_template("index.html")


# Application error handlers
@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error=None):
    message = {
            'code': error.code,
            'status': 'failure',
            'url': request.url,  # set the requested url
            'reason': error.name
    }
    resp = jsonify(message)  # generate a response object
    resp.status_code = error.code  # set the error status code
    return resp