import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class User(db.Model):
  __bind_key__ = 'users'
  
  userId = db.Column(db.Integer, primary_key=True)
  customerId = db.Column(db.Integer)
  branchId = db.Column(db.Integer)
  username = db.Column(db.String(100))
  password = db.Column(db.String(100))
  userType = db.Column(db.Integer)
  firstName = db.Column(db.String(255))
  lastName = db.Column(db.String(255))
  email = db.Column(db.String(255))
  resellerId = db.Column(db.Integer)
  enabled = db.Column(db.Boolean)
  isSalesRep = db.Column(db.Boolean)
  agentId = db.Column(db.Integer)
  failedLogins = db.Column(db.Integer)
  lockedOut = db.Column(db.DateTime)
  lockouts = db.Column(db.Integer)
  lnpRecipient = db.Column(db.Boolean)
  timezone = db.Column(db.String(255))
  contactType = db.Column(db.Integer)
  organization_id = db.Column(db.BigInteger)
  role_id = db.Column(db.BigInteger)
  addressId = db.Column(db.Integer)
  chat_token = db.Column(db.String(100))
  avatar_id = db.Column(db.BigInteger)
  lastLoginTime = db.Column(db.DateTime)
  
  def __init__(self,
               customerId,
               branchId,
               username,
               password,
               userType,
               firstName,
               lastName,
               email,
               resellerId,
               enabled,
               isSalesRep,
               agentId,
               failedLogins,
               lockedout,
               lockouts,
               lnpRecipient,
               timezone,
               contactType,
               organization_id,
               role_id,
               addressId,
               chat_token,
               avatar_id,
               lastLoginTime):
    self.customerId = customerId
    self.branchId = branchId
    self.username = username
    self.password = password
    self.userType = userType
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.resellerId = resellerId
    self.enabled = enabled
    self.isSalesRep = isSalesRep
    self.agentId = agentId
    self.failedLogins = failedLogins
    self.lockedout = lockedout
    self.lockouts = lockouts
    self.lnpRecipient = lnpRecipient
    self.timezone = timezone
    self.contactType = contactType
    self.organization_id = organization_id
    self.role_id = role_id
    self.addressId = addressId
    self.chat_token = chat_token
    self.avatar_id = avatar_id
    self.lastLoginTime = lastLoginTime
