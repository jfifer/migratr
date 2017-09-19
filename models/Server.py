import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class Server(db.Model):
  __bind_key__ = 'server'
  serverId = db.Column(db.Integer, primary_key=True)
  serverType = db.Column(db.Integer)
  name = db.Column(db.String(255))
  hostname = db.Column(db.String(255))
  ipAddress = db.Column(db.String(255))
  localtion = db.Column(db.String(255))
  serverUsername = db.Column(db.String(255))
  serverPassword = db.Column(db.String(255))
  connection = db.Column(db.String(255))
  note = db.Column(db.Text)
  serverStatus = db.Column(db.Integer)
  registrationId = db.Column(db.Integer)
  resellerId = db.Column(db.Integer)
  customerId = db.Column(db.Integer)
  serverGroupId = db.Column(db.Integer)
  dialplanDbHost = db.Column(db.String(255))
  dialplanDbUser = db.Column(db.String(255))
  dialplanDbPass = db.Column(db.String(255))
  dialplanDbName = db.Column(db.String(255))
  dialplanDbPort = db.Column(db.String(255))
  cdrDbHost = db.Column(db.String(255))
  cdrDbUser = db.Column(db.String(255))
  cdrDbPass = db.Column(db.String(255))
  cdrDbName = db.Column(db.String(255))
  cdrDbPort = db.Column(db.String(255))
  regServerHostname = db.Column(db.String(255))
  amiHost = db.Column(db.String(255))
  amiPort = db.Column(db.String(255))
  amiUser = db.Column(db.String(255))
  amiPass = db.Column(db.String(255))
  ftpHost = db.Column(db.String(255))
  ftpPort = db.Column(db.String(255))
  ftpUser = db.Column(db.String(255))
  ftpPass = db.Column(db.String(255))
  routingDbHost = db.Column(db.String(255))
  routingDbUser = db.Column(db.String(255))
  routingDbPass = db.Column(db.String(255))
  routingDbName = db.Column(db.String(255))
  routingDbPort = db.Column(db.String(255))
  subscriberDbHost = db.Column(db.String(255))
  subscriberDbUser = db.Column(db.String(255))
  subscriberDbPass = db.Column(db.String(255))
  subscriberDbName = db.Column(db.String(255))
  subscriberDbPort = db.Column(db.String(255))
  priority = db.Column(db.Integer)
  mountpoint = db.Column(db.String(255))
  isMultiTenant = db.Column(db.Boolean)
  asteriskListeningPOrt = db.Column(db.Integer)
  xmppHost = db.Column(db.String(255))
  xmppPort = db.Column(db.Integer)
  boshURL = db.Column(db.String(255))
  boshPort = db.Column(db.String(255))
  fax = db.Column(db.Integer)
  channelPathRatio = db.Column(db.Integer)
  platformId = db.Column(db.Integer)
  provisioningFilePath = db.Column(db.String(255))
  isPrimary = db.Column(db.Integer)
  provisioningHost = db.Column(db.String(255))
  provisioningPass = db.Column(db.String(255))
  provisioningPort = db.Column(db.String(255))
  provisioningUser = db.Column(db.String(255))
  provisioningName = db.Column(db.String(255))
  sipProxyGroupId = db.Column(db.String(255))
  timezone = db.Column(db.String(255))

  def __init__(self,
               serverTypeId,
               name,
               hostname,
               ipAddress,
               location,
               serverUsername,
               serverPassword,
               connection,
               note,
               serverStatus,
               registrationId,
               resellerId,
               customerId,
               serverGroupId,
               dialplanDbHost,
               dialplanDbUser,
               dialplanDbPass,
               dialplanDbPort,
               cdrDbHost,
               cdrDbUser,
               cdrDbPass,
               cdrDbPort,
               regServerHostname,
               amiHost,
               amiPort,
               amiUser,
               amiPass,
               ftpHost,
               ftpPort,
               ftpUser,
               ftpPass,
               routingDbHost,
               routingDbUser,
               routingDbPass,
               routingDbName,
               routingDbPort,
               subscriberDbHost,
               subscriberDbUser,
               subscriberDbPass,
               subscriberDbName,
               subscriberDbPort,
               priority,
               mountPoint,
               isMultiTenant,
               asteriskListeningPort,
               xmppHost,
               xmppPOrt,
               boshURL,
               boshPort,
               fax,
               channelPathRatio,
               platformId,
               provisioningFilePath,
               isPrimary,
               provisioningHost,
               provisioningPass,
               provisioningPort,
               provisioningUser,
               provisioningName,
               sipProxyGroupId,
               timezone):
    self.serverTypeId = serverTypeId
    self.name = name
    self.hostname = hostname
    self.ipAddress = ipAddress
    self.location = location
    self.serverUsername = serverUsername
    self.serverPassword = serverPassword
    self.connection = connection
    self.note = note
    self.serverStatus = serverStatus
    self.registrationId = registrationId
    self.resellerId = resellerId
    self.customerId = customerId
    self.serverGroupId = serverGroupId
    self.dialplanDbHost = dialplanDbHost
    self.dialplanDbUser = dialplanDbUser
    self.dialplanDbPass = dialplanDbPass
    self.dialplanDbName = dialplanDbName
    self.dialplanDbPort = dialplanDbPort
    self.cdrDbHost = cdrDbHost
    self.cdrDbUser = cdrDbUser
    self.cdrDbPass = cdrDbPass
    self.cdrDbName = cdrDbName
    self.cdrDbPort = cdrDbPort
    self.regServerHostname = regServerHostname
    self.amiHost = amiHost
    self.amiPort = amiPort
    self.amiUser = amiUser
    self.amiPass = amiPass
    self.ftpHost = ftpHost
    self.ftpPort = ftpPort
    self.ftpUSer = ftpUser
    self.ftpPass = ftpPass
    self.routingDbHost = routingDbHost
    self.routingDbUser = routingDbUser
    self.routingDbPass = routingDbPass
    self.routingDbName = routingDbName
    self.routingDbPort = routingDbPort
    self.priority = priority
    self.mountPoint = mountPoint
    self.isMultiTenant = isMultiTenant
    self.asteriskListeningPort = asteriskListeningPort
    self.xmppHost = xmppHost
    self.xmppPort = xmppPort
    self.boshURL = boshURL
    self.boshPort = boshPort
    self.fax = fax
    self.channelPathRatio = channelPathRatio
    self.platformId = platformId
    self.provisioningFilePath = provisioningFilePath
    self.isPrimary = isPrimary
    self.provisioningHost = provisioningHost
    self.provisioningPass = provisioningPass
    self.provisioningPort = provisioningPort
    self.provisioningUser = provisioningUser
    self.provisioningName = provisioningName
    self.sipProxyGroupId = sipProxyGroupId
    self.timezone = timezone
