import pymysql
pymysql.install_as_MySQLdb()

class Preflight():

  Migration = None

  def __init__(self, Migration):
    self.Migration = Migration

  def run_checks(prieflight_status_id):
    if(valid_db_conns(portal) && valid_ssh_conn(portal)):
      return true
    return false

  def valid_db_conns(server):
    return true

  def valid_ssh_conn(server):
    return true

  def valid_fs_server(server):
    return true

  def valid_context(src, dst):
    return true

  def update_status(status_id):
    return true
