import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class Customer(db.Model):
  __bind_key__ = 'customer'
  customerId = db.Column(db.Integer, primary_key=True)
  resellerId = db.Column(db.Integer)
  accountId = db.Column(db.Integer)
  companyName = db.Column(db.String(255))
  partnerAgentId = db.Column(db.Integer)
  phone = db.Column(db.String(30))
  fax = db.Column(db.String(30))
  email = db.Column(db.String(255))
  billingEmail = db.Column(db.String(255))
  techEmail = db.Column(db.String(255))
  ccNumber = db.Column(db.String(255))
  ccType = db.Column(db.String(255))
  ccExpireDate = db.Column(db.DateTime)
  ccNameOnCard = db.Column(db.String(255))
  perMinuteRate = db.Column(db.Float(7,6))
  perMinuteRateTollFree = db.Column(db.Float(7,6))
  meetMeRate = db.Column(db.Float(7,6))
  perTranscriptionRate = db.Column(db.Float(8,6))
  billingAddressId = db.Column(db.Integer)
  shippingAddressId = db.Column(db.Integer)
  taxJurisdictionId = db.Column(db.Integer)
  anniversaryDate = db.Column(db.Integer)
  paymentMethodId = db.Column(db.Integer)
  maxPaths = db.Column(db.Integer)
  statusId = db.Column(db.Integer)
  salesRepId = db.Column(db.Integer)
  planType = db.Column(db.Integer)
  originalActivationDate = db.Column(db.DateTime)
  cancellationDate = db.Column(db.DateTime)
  note = db.Column(db.Text)
  hostedFaxEnabled = db.Column(db.Integer)
  hostedFaxTermsApproved = db.Column(db.Integer)
  hostedFaxSenders = db.Column(db.Integer)
  hostedFaxPerPageRate = db.Column(db.Float(8,6))
  timezone = db.Column(db.String(255))
  dashboard_subscriptions = db.Column(db.Integer)
  due_date_offset = db.Column(db.Integer)
  dunning_emails_disabled = db.Column(db.Boolean)
  dunning_charge_disabled = db.Column(db.Boolean)
  networkToolEnabled = db.Column(db.Boolean)
  ccProfileId = db.Column(db.String(255))
  defaultCCPaymentProfileId = db.Column(db.Integer)
  referring_organization_id = db.Column(db.Integer)
  invoice_download_expiration = db.Column(db.Integer)
  siteAddressUpdateFailed = db.Column(db.Boolean)
  siteAddressId = db.Column(db.Integer)
  externalAccountId = db.Column(db.String(255))
  platformId = db.Column(db.Integer)
  extensionLength = db.Column(db.Integer)

  def __init__(self,
               resellerId,
               accountId,
               companyName,
               partnerAgentId,
               phone,
               fax,
               email,
               billingEmail,
               techEmail,
               ccNumber,
               ccType,
               ccExpireDate,
               ccNameOnCard,
               perMinuteRate,
               perMinuteRateTollFree,
               meetMeRate,
               perTranscriptionRate,
               billingAddressId,
               shippingAddressId,
               taxJurisdictionId,
               anniversaryDate,
               paymentMethodId,
               maxPaths,
               statusId,
               salesRepId,
               planType,
               originalActivationDate,
               cancellationDate,
               note,
               hostedFaxEnabled,
               hostedFaxTermsApproved,
               hostedFaxSenders,
               hostedFaxPerPageRate,
               timezone,
               dashboard_subscriptions,
               due_date_offset,
               dunning_emails_disabled,
               dunning_charge_disabled,
               networkToolEnabled,
               ccProfileId,
               defaultCCPaymentProfileId,
               referring_organization_id,
               invoice_download_expiration,
               siteAddressUpdateFailed,
               siteAddressId,
               externalAccountId,
               platformId,
               extensionLength):
    self.resellerId = resellerId
    self.accountId = accountId
    self.companyName = companyName
    self.partnerAgentId = partnerAgentId
    self.phone = phone
    self.fax = fax
    self.email = email
    self.billingEmail = billingEmail
    self.techEmail = techEmail
    self.ccNumber = ccNumber
    self.ccType = ccType
    self.ccExpireDate = ccExpireDate
    self.ccNameOnCard = ccNameOnCard
    self.perMinuteRate = perMinuteRate
    self.perMinuteRateTollFree = perMinuteRateTollFree
    self.meetMeRate = meetMeRate
    self.perTranscriptionRate = perTranscriptionRate
    self.billingAddressId = billingAddressId
    self.shippingAddressId = shippingAddressId
    self.taxJurisdictionId = taxJurisdictionId
    self.anniversaryDate = anniversaryDate
    self.paymentMethodId = paymentMethodId
    self.maxpaths = maxpaths
    self.statusId = statusId
    self.salesRepId = salesRepId
    self.planType = planType
    self.originalActivationDate = originalActivationDate
    self.cancellationDate = cancellationDate
    self.note = note
    self.hostedFaxEnabled = hostedFaxEnabled
    self.hostedFaxTermsApproved = hostedFaxTermsApproved
    self.hostedFaxSenders = hostedFaxSenders
    self.hostedFaxPerPageRate = hostedFaxPerPageRate
    self.timezone = timezone
    self.dashboard_subscriptions = dashboard_subscriptions
    self.due_date_offset = due_date_offset
    self.dunning_emails_disabled = dunning_emails_disabled
    self.dunning_charge_disabled = dunning_charged_disabled
    self.networkToolEnabled = networkToolEnabled
    self.ccProfileId = ccProfileId
    self.defaultCCPaymentProfileId = defaultCCPaymentProfileId
    self.referring_organization_id = referring_organization_id
    self.invoice_download_expiration = invoice_download_expiration
    self.siteAddressUpdateFailed = siteAddressUpdateFailed
    self.siteAddressId = siteAddressId
    self.externalAccountId = externalAccountId
    self.platformId = platformId
    self.extensionLength = extensionLength
