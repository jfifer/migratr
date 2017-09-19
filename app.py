from functools import wraps
from flask import Flask, flash, redirect, render_template, request, Response, session, abort, jsonify
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text, exc
from sqlalchemy.orm import sessionmaker
from models.User import User
from models.Reseller import Reseller
from models.Customer import Customer
from models.Branch import Branch
from models.Server import Server
from models.ServerGroup import ServerGroup
from models.Migration import Migration
from models.DelayedJobs import DelayedJobs
from models.MigrationMetrics import MigrationMetrics
from controllers.Preflight import Preflight
import os
import sys
import json
import datetime
import time

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = sqlalchemy(app)

portal = create_engine("mysql://spbilling:b1cycl3s@backup-db.webapp.coredial.com/portal")
PortalDB = sessionmaker(bind=portal)
cnx = PortalDB()

migratr = create_engine("mysql://root:narwhal@localhost/migratr")
MigratrDB = sessionmaker(bind=migratr)
migratrCNX = MigratrDB()

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
    return render_template('home.html')

@app.route("/login", methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    Session = sessionmaker(bind=portal)
    cnx = Session()
    result = cnx.query(User).filter("username='"+username+"' AND password=SHA1('"+password+"')").first()
    cnx.commit()
    
    if result is None:
        session['logged_in'] = False
        return redirect('/')
    session['logged_in'] = True
    return redirect('/')

@app.route("/new")
@requires_auth
def new(): 
    return render_template("new.html")

@app.route("/partner/<string:partner>", methods=['GET'])
@requires_auth
def partnerSeach(partner):
    result = cnx.query(Reseller.resellerId, Reseller.companyName).filter("companyName LIKE '"+partner+"%'").all()
    cnx.commit()
    return jsonify(dict(result))

@app.route("/customer/<int:resellerId>/<string:customer>", methods=['GET'])
@requires_auth
def customerSearch(resellerId, customer):
    result = cnx.query(Customer.customerId, Customer.companyName).filter("companyName LIKE '"+customer+"%' AND resellerId="+str(resellerId)).all()
    cnx.commit()
    return jsonify(dict(result))

@app.route("/pbx/<int:resellerId>/<string:context>", methods=['GET'])
@requires_auth
def pbxSearch(resellerId, context):
    result = cnx.query(Branch.branchId, Branch.description).filter("description LIKE '"+context+"%' AND resellerId="+str(resellerId)).all()
    cnx.commit()
    return jsonify(dict(result))

@app.route("/pbx/<int:customerId>", methods=['GET'])
@requires_auth
def getContextByCustomer(customerId):
    result = cnx.query(Branch.branchId, Branch.description, Customer.companyName).filter("customer.customerId="+str(customerId)).first()
    cnx.commit()
    return jsonify(dict(result))

@app.route("/server/reseller/<int:resellerId>", methods=['GET'])
@requires_auth
def getGroups(resellerId):
  result = cnx.query(ServerGroup.serverGroupId, ServerGroup.name).filter("resellerId="+str(resellerId)).all()
  cnx.commit()
  return jsonify(dict(result))

@app.route("/server/group/<int:groupId>/<string:hostname>/<int:status>", methods=['GET'])
@requires_auth
def getServersByGroup(groupId, hostname, status):
  statusQry = "serverStatus = 1"
  if status is 2:
      statusQry = "serverStatus <> 0"
  result = cnx.query(Server.serverId, Server.hostname).filter("serverGroupId="+str(groupId)+" AND hostname LIKE '"+hostname+"%' AND "+statusQry).all()
  cnx.commit()
  return jsonify(dict(result))

@app.route("/server/<string:hostname>/<int:status>", methods=['GET'])
@requires_auth
# 0-inactive, 1-open, 2-closed
def getServers(hostname, status):
    statusQry = "serverStatus = 1"
    if status is 2:
        statusQry = "serverStatus <> 0"
    result = cnx.query(Server.serverId, Server.hostname).filter(statusQry+" AND hostname LIKE '"+hostname+"%'").all()
    cnx.commit()
    return jsonify(dict(result))

@app.route("/migrations/<int:runat>/<string:sortby>/<string:sorthow>", methods=['GET'])
@requires_auth
def getMigrationsByTime(runat, sortby='id', sorthow='ASC'):
    query = migratrCNX.query(Migration).filter("TIMESTAMP(run_at) IS NOT NULL AND TIMESTAMP(run_at) > '"+str(runat)+"'")
    if sorthow is 'DESC':
        result = query.order_by(desc(getattr(Migration, sortby))).all()
    else:
        result = query.order_by(getattr(Migration, sortby)).all()
    migratrCNX.commit()
    if result is None:
        return "No Results"
    data = []
    for res in result:
        data.append({"id": res[0]})
    return data

@app.route("/test", methods=['GET'])
def test():
    test = Preflight.sendBackShit()
    return render_template('test.html', test=test)

@app.route("/migrationsold/<int:runat>/<string:sortby>/<string:sorthow>", methods=['GET'])
@requires_auth
def getMigrationsByTimeold(runat, sortby='id', sorthow='ASC'):
    db = create_engine('mysql://root:narwhal@localhost/migratr')
    cnx = db.connect()
    run_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(runat))
    query = "SELECT * from migrations where TIMESTAMP(run_at) IS NOT NULL AND TIMESTAMP(run_at) > '%s' ORDER BY %s %s" % (run_at, sortby, sorthow)
    result = cnx.execute(text(query)).fetchall()
    data = []
    for res in result:
      data.append({"id": res[0],
        "src_server": res[2],
        "dst_server": res[4],
        "context": res[5],
        "customer": res[8],
        "reseller": res[10],
        "run_at": res[11],
        "state": res[12]
      })
    return jsonify(data)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)
