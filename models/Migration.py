import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class Migration(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  src_server_id = db.Column(db.Integer)
  src_server_name = db.Column(db.String(255))
  dst_server_id = db.Column(db.Integer)
  dst_server_name = db.Column(db.String(255))
  context = db.Column(db.String(255))
  branch_id = db.Column(db.Integer)
  customer_id = db.Column(db.Integer)
  customer_name = db.Column(db.String(255))
  reseller_id = db.Column(db.Integer)
  reseller_name = db.Column(db.String(255))
  run_at = db.Column(db.DateTime)
  state = db.Column(db.String(255))
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  activity_cursor = db.Column(db.DateTime)
  email_addresses = db.Column(db.Text)
  job_id = db.Column(db.Integer)

  def __init__(self,
               src_server_id,
               src_server_name,
               dst_server_id,
               dst_server_name,
               context,
               branch_id,
               customer_id,
               customer_name,
               reseller_id,
               reseller_name,
               run_at,
               state,
               created_at,
               updated_at,
               activity_cursor,
               email_addresses,
               job_id):
    self.src_server_id = src_server_id
    self.src_server_name = src_server_name
    self.dst_server_id = dst_server_id
    self.dst_server_name = dst_server_name
    self.context = context
    self.branch_id = branch_id
    self.customer_id = customer_id
    self.customer_name = customer_name
    self.reseller_id = reseller_id
    self.reseller_name = reseller_name
    self.run_at = run_at
    self.created_at = created_at
    self.updated_at = updated_at
    self.activity_cursor = activity_cursor
    self.email_addresses = email_addresses
    self.job_id
