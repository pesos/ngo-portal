# Local project imports
from core import app
from core.models import User
import helpers as util

# Standard python imports
import json

# Third party imports
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")
