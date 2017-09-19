import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class ServerGroup(db.Model):
  __bind_key__ = 'serverGroup'
  __tablename__ = 'serverGroup'
  serverGroupId = db.Column(db.Integer, primary_key=True)
  serverTypeId = db.Column(db.Integer)
  resellerId = db.Column(db.Integer)
  isSystemGroup = db.Column(db.Integer)
  name = db.Column(db.String(255))

  def __init__(self,
               serverTypeId,
               resellerId,
               isSystemGroup,
               name):
    self.serverTypeId = serverTypeId
    self.resellerId = resellerId
    self.isSystemGroup = isSystemGroup
    self.name = name

