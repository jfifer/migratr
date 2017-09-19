import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class PreflightStatus(db.Model):
  __bind_key__ = 'preflight_statuses'
  __tablename__ = 'preflight_statuses'
  id = db.Column(db.Integer, primary_key=True)
  migration_id = db.Column(db.Integer)
  portal_connection_state = db.Column(db.String(255))
  src_connection_state = db.Column(db.String(255))
  dst_connection_state = db.Column(db.String(255))
  api_connection_state = db.Column(db.String(255))
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  metrics = db.Column(db.String(255))
  final = db.Column(db.String(255))

  def __init__(self,
               migration_id,
               portal_connection_state,
               src_connection_state,
               dst_connection_state,
               api_connection_state,
               created_at,
               updated_at,
               metrics,
               final):
    self.migration_id = migration_id
    self.portal_connection_state = portal_connection_state
    self.src_connection_state = src_connection_state
    self.dst_connection_state = dst_connection_state
    self.api_connection_state = api_connection_state
    self.created_at = created_at
    self.updated_at = updated_at
    self.metrics = metrics
    self.final = final
