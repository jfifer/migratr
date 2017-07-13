from functools import wraps
from flask import Flask, flash, redirect, render_template, request, Response, session, abort, jsonify
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
import os
import sys
import json

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

app = Flask(__name__)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('logged_in'):
            return render_template('login.html')
        return f(*args, **kwargs)
    return decorated

@app.route("/")
@requires_auth
def index():
    return render_template(
        'home.html')

@app.route("/partner/<string:partner>", methods=['GET'])
@requires_auth
def partnerSearch(partner):
    db = create_engine('mysql://spbilling:b1cycl3s@backup-db.webapp.coredial.com/portal')
    cnx = db.connect()
    query = "SELECT resellerId, companyName FROM reseller WHERE companyName LIKE '%s'" % (partner+'%')
    result = cnx.execute(text(query)).fetchall()
    return jsonify(dict(result))
 
@app.route("/login", methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']
    db = create_engine('mysql://spbilling:b1cycl3s@backup-db.webapp.coredial.com/portal')
    cnx = db.connect()
    query = "SELECT userId FROM user WHERE email='%s' AND password=SHA1('%s')" % (user, password)
    
    result = cnx.execute(text(query))
    row = result.fetchone()
    if row is None:
        session['logged_in'] = False
        return "-1"
    session['logged_in'] = True
    return redirect("/")
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)