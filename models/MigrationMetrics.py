import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class MigrationMetrics(db.Model):
  __bind_key__ = 'migration_metrics'
  __tablename__ = 'migration_metrics'
  id = db.Column(db.Integer, primary_key=True)
  source_include_line_count = db.Column(db.Integer)
  migration_id = db.Column(db.Integer)
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)
  destination_include_line_count = db.Column(db.Integer)
  source_mailbox_count = db.Column(db.Integer)
  source_aa_recording_count = db.Column(db.Integer)
  source_sip_endpoint_count = db.Column(db.Integer)
  source_context_line_count = db.Column(db.Integer)
  source_endpoint_ips = db.Column(db.Text)

  def __init__(self,
               source_include_line_count,
               migration_id,
               created_at,
               updated_at,
               destination_include_line_count,
               source_mailbox_count,
               source_aa_recording_count,
               source_sip_endpoint_count,
               source_context_line_count,
               source_endpoint_ips):
    self.source_include_line_count = source_include_line_count
    self.migration_id = migration_id
    self.created_at = created_at
    self.updated_at = updated_at
    self.destination_include_line_count = destination_include_line_count
    self.source_mailbox_count = source_mailbox_count
    self.source_aa_recording_count = source_aa_recording_count
    self.source_sip_endpoint_count = source_sip_endpoint_count
    self.source_context_line_count = source_context_line_count
    self.source_endpoint_ips = source_endpoint_ips
