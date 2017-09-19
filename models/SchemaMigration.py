import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy as sqlalchemy
from sqlalchemy import create_engine, text

db = sqlalchemy()

class SchemaMigration(db.Model):
  __bind_key__ = 'schema_migrations'
  __tablename__ = 'schema_migrations'
  version = db.Column(db.String(255))

  __init__(self, version):
    self.version = version

