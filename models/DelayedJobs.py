import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class DelayedJobs(db.Model):
  __bind_key__ = 'reseller'
  __tablename__ = 'delayed_jobs'
  id = db.Column(db.Integer, primary_key=True)
  priority = db.Column(db.Integer)
  attempts = db.Column(db.Integer)
  handler = db.Column(db.Text)
  last_error = db.Column(db.Text)
  run_at = db.Column(db.DateTime)
  locked_at = db.Column(db.DateTime)
  failed_at = db.Column(db.DateTime)
  locked_by = db.Column(db.String(255))
  queue = db.Column(db.String(255))
  created_at = db.Column(db.DateTime)
  updated_at = db.Column(db.DateTime)

  def __init__(self,
               priority,
               attempts,
               handler,
               last_error,
               run_at,
               locked_at,
               failed_at,
               locked_by,
               queue,
               created_at,
               updated_at):
    self.priority = priority
    self.attempts = attempts
    self.handler = handler
    self.last_error = last_error
    self.run_at = run_at
    self.locked_at = locked_at
    self.failed_at = failed_at
    self.locked_by = locked_by
    self.queue = queue
    self.created_at = created_at
    self.updated_at = updated_at
