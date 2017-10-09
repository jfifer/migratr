from paramiko import client
import pymysql
pymysql.install_as_MySQLdb()

class Preflight():

  Migration = None

  def __init__(self, Migration):
    self.Migration = Migration

  def run_checks(preflight_status_id):
    return valid_db_conns

  def valid_db_conns(server):
    return "db-"+server

  def valid_ssh_conn(server):
    client = client.SSHClient()
    client.set_missing_host_key_policy(client.AutoAddPolicy())
    client.connect('bongo.coredial.com', username='jfifer', password='RedSky!2012!', look_for_keys=False)

  def valid_fs_server(server):
    return true

  def valid_context(src, dst):
    return true

  def update_status(status_id):
    return true
