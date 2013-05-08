# Local project imports
from core import app
from core.models import User
import helpers as util

# Standard python imports
import json
from models import *
# Third party imports
from flask import render_template, jsonify, request

# Application homepage
@app.route('/index')
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method == 'POST':
        user = User(request.form['first_name'], request.form['last_name'], request.form['date_of_birth'], request.form['college'], request.form['year_of_study'], request.form['branch'], request.form['blood_group'], request.form['email'], request.form['news'], request.form['phone'], request.form['address'], request.form['facebook'], request.form['linkedin'], request.form['twitter'], request.form['google'], request.form['pintrest'], request.form['role'],request.form['blood'],request.form['organ'],request.form['disaster'])
        db.session.add(user)
        db.session.commit()
        return render_template("register.html", user.first_name)

@app.route('/copyright')
def copyright():
    return "Copyright Message Here"

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

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