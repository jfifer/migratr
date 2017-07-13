from functools import wraps
from flask import Flask, flash, redirect, render_template, request, Response, session, abort
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
    def decorated(*args):
        if not session.get('logged_in'):
            return render_template('login.html')
        return f()
    return decorated

@app.route("/")
@requires_auth
def index():
    return render_template(
        'home.html')

@app.route("/partner/:partner")

@app.route("/partnerSearch", methods=['GET', 'POST'])
@requires_auth
def partnerSearch():
    reseller = request.form['reseller']
    custPbx = request.form['customer']
    
    query = """select r.companyName, b.description, c.companyName
            FROM reseller r
            JOIN branch b on b.resellerId=r.resellerId
            JOIN customer c on c.customerId=b.customerId
            WHERE r.companyName LIKE '%s' AND (c.companyName LIKE '%s' OR b.description LIKE '%s')""" % (reseller+'%', custPbx+'%', custPbx+'%')
    return query;
    
 
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