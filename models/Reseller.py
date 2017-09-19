import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class Reseller(db.Model):
  __bind_key__ = 'reseller'
  resellerId = db.Column(db.Integer, primary_key=True)
  companyName = db.Column(db.String(255))
  identifier = db.Column(db.String(255))
  tier = db.Column(db.Integer)
  addressId = db.Column(db.Integer)
  email = db.Column(db.String(255))
  phone = db.Column(db.String(255))
  billingOptOut = db.Column(db.Boolean)
  pageHeader = db.Column(db.Text)
  pageFooter = db.Column(db.Text)
  e911Terms = db.Column(db.Text)
  oneTimePaymentTerms = db.Column(db.Text)
  prefix = db.Column(db.String(25))
  defaultTaxJurisdictionId = db.Column(db.Integer)
  callRecordingDisclaimer = db.Column(db.Text)
  themeName = db.Column(db.String(255))
  cnamStorage = db.Column(db.Boolean)
  cnamDipAuthorized = db.Column(db.Boolean)
  cloudExtensionsEnabled = db.Column(db.String(45))
  allowInternational = db.Column(db.Boolean)
  internationalDefault = db.Column(db.Boolean)
  parentResellerId = db.Column(db.Integer)
  showPoweredByOnLogin = db.Column(db.Boolean)
  showPoweredByToCustomers = db.Column(db.Boolean)
  oneTimePaymentTermsACH = db.Column(db.Text)
  hostedFaxEnabled = db.Column(db.Integer)
  timezone = db.Column(db.String(255))
  customCIDEnabled = db.Column(db.Boolean)
  sipProxyEnabled = db.Column(db.Boolean)
  active_theme_id = db.Column(db.Integer)
  status_id = db.Column(db.Integer)
  default_invoice_download_expiration = db.Column(db.Integer)
  voiceTranscriptionEnabled = db.Column(db.Boolean)
  sdwanEnabled = db.Column(db.Boolean)

  def __init__(self,
               companyName,
               identifier,
               tier,
               addressId,
               email,
               phone,
               billingOptOut,
               pageHeader,
               pageFooter,
               e911Terms,
               oneTimePaymentTerms,
               prefix,
               defaultTaxJurisdictionId,
               callRecordingDisclaimer,
               themeName,
               cnamStorage,
               cnamDipAuthorized,
               cloudExtensionsEnabled,
               allowInternational,
               internationalDefault,
               parentResellerId,
               showPoweredByOnLogin,
               showPoweredByToCustomers,
               oneTimePaymentTermsACH,
               hostedFaxEnabled,
               timezone,
               customCIDEnabled,
               sipProxyEnabled,
               active_theme_id,
               status_id,
               default_invoice_download_expiration,
               voiceTranscriptionEnabled,
               sdwanEnabled):
    self.companyName = companyName
    self.identifier = identifier
    self.tier = tier
    self.addressId = addressId
    self.email = email
    self.phone = phone
    self.billingOptOut = billingOptOut
    self.pageHeader = pageHeader
    self.pageFooter = pageFooter
    self.e911Terms = e911Terms
    self.oneTimePaymentTerms = oneTimePaymentTerms
    self.prefix = prefix
    self.defaultTaxJurisdictionId = defaultTaxJurisdictionId
    self.callRecordingDisclaimer = callRecordingDisclaimer
    self.themeName = themeName
    self.cnamStorage = cnamStorage
    self.cnamDipAuthorized = cnamDipAuthorized
    self.cloudExtensionsEnabled = cloudExtensionsEnabled
    self.allowInternational = allowInternational
    self.internationalDefault = internationalDefault
    self.parentResellerId = parentResellerId
    self.showPoweredByOnLogin = showPoweredByOnLogin
    self.showPoweredByToCustomers = showPoweredByToCustomers
    self.oneTimePaymentTermsACH = oneTimePaymentTermsACH
    self.hostedFaxEnabled = hostedFaxEnabled
    self.timezone = timezone
    self.customCIDEnabled = customCIDEnabled
    self.sipProxyEnabled = sipProxyEnabled
    self.active_theme_id = active_theme_id
    self.status_id = status_id
    self.default_invoice_download_expiration = default_invoice_download_expiration
    self.voiceTranscriptionEnabled = voiceTranscriptionEnabled
    self.sdwanEnabled = sdwanEnabled
