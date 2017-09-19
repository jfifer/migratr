import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text, ForeignKey
from sqlalchemy.orm import relationship
from models.Customer import Customer

db = sqlalchemy()

class Branch(db.Model):
  __bind_key__ = 'branch'
  branchId = db.Column(db.Integer, primary_key=True)
  resellerId = db.Column(db.Integer, ForeignKey('reseller.resellerId'))
  customerId = db.Column(db.Integer, ForeignKey('customer.customerId'))
  siteId = db.Column(db.Integer)
  registrationTypeId = db.Column(db.Integer)
  dialplanTypeId = db.Column(db.Integer)
  federationId = db.Column(db.Integer)
  featureServerId = db.Column(db.Integer)
  faxServerId = db.Column(db.Integer)
  clusterId = db.Column(db.Integer)
  description = db.Column(db.Text)
  callerId = db.Column(db.String(255))
  callerIdName = db.Column(db.String(255))
  international = db.Column(db.String(1))
  cpniPin = db.Column(db.String(255))
  enablePickup = db.Column(db.Boolean)
  enableCallCenter = db.Column(db.Boolean)
  NPA = db.Column(db.String(3))
  enableSevenDigitDialing = db.Column(db.Boolean)
  enableIntercom = db.Column(db.Boolean)
  enableCallRecording = db.Column(db.Boolean)
  enableVoiceTranscription = db.Column(db.Boolean)
  cnamStorage = db.Column(db.Boolean)
  cnamDipAuthorized = db.Column(db.Boolean)
  enableDirectoryByFirstName = db.Column(db.Boolean)
  enableDirectoryExtensionRead = db.Column(db.Boolean)
  callParkTimeout = db.Column(db.Integer)
  polycomOSId = db.Column(db.Integer)
  allowInternational = db.Column(db.Boolean)
  obfuscatedDir = db.Column(db.String(255))
  internationalPin = db.Column(db.String(10))
  internationalPinTimeout = db.Column(db.Integer)
  internationalTimeFrame = db.Column(db.Text)
  isProvisioned = db.Column(db.Integer)
  sipProxyType = db.Column(db.Integer)

  #customer_branch_fk = relationship("Customer", foreign_keys=[customerId])
  #branch_reseller_ibfk_1 = relationship("Reseller", foreign_keys=[resellerId])

  def __init__(self,
               resellerId,
               customerId, 
               siteId,
               registrationTypeId,
               dialplanTypeId,
               federationId,
               featureServerId,
               faxServerId,
               clusterId,
               description,
               callerId,
               callerIdName,
               international,
               cpniPin,
               enablePickup,
               enableCallCenter,
               NPA,
               enableSevenDigitDialing,
               enableIntercom,
               enableCallRecording,
               enableVoiceTranscription,
               cnamStorage,
               cnamDipAuthorized,
               enableDirectoryByFirstName,
               enableDirectoryExtensionRead,
               callParkTimeout,
               polycomOSId,
               allowInternational,
               obfuscatedDir,
               internationalPin,
               internationalPinTimeout,
               internationalPinTimeFrame,
               isProvisioned,
               sipProxyType):
    self.resellerId = resellerId
    self.customerId = customerId
    self.siteId = siteId
    self.registrationTypeId = registrationTypeId
    self.dialplanTypeId = dialplanTypeId
    self.federationId = federationId
    self.featureServerId = featureServerId
    self.faxServerId = faxServerId
    self.clusterId = clusterId
    self.description = description
    self.callerId = callerId
    self.callerIdName = callerIdName
    self.international = international
    self.cpniPin = cpniPin
    self.enablePickup = enablePickup
    self.enableCallCenter = enableCallCenter
    self.NPA = NPA
    self.enableSevenDigitDialing = enableSevenDigitDialing
    self.enableIntercom = enableIntercom
    self.enableCallRecording = enableCallRecording
    self.enableVoiceTranscriptions = enableVoiceTranscriptions
    self.cnamStorage = cnamStorage
    self.cnamDipAuthorized = cnamDipAuthorized
    self.enableDirectoryByFirstName = enableDirectoryByFirstName
    self.enableDirectoryExtensionRead = enableDirectoryExtensionRead
    self.callParkTimeout = callParkTimeout
    self.polycomOSId = polycomOSId
    self.allowInternational = allowInternational
    self.obfuscatedDir = obfuscatedDir
    self.internationalPin = InternationalPin
    self.internationalPinTimeout = internationalPinTimeout
    self.internationalPinTimeFrame = internationalPinTimeFrame
    self.isProvisioned = isProvisioned
    self.sipProxyType = sipProxyType
