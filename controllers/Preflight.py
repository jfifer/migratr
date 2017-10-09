from paramiko import client
import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, jsonify
import json

class Preflight():

  Migration = None
  portal_host = "jobs1.webapp.coredial.com"
  portal_db_host = "db.webapp.coredial.com"
  portal_db_user = "portal"
  portal_db_pass = "*****"
  portal_db_name = "portal"

  def __init__(self, Migration):
    self.Migration = Migration

  def run_checks(preflight_status_id):
    return valid_db_conns

  def valid_db_conns(server):
    return "db-"+server

  def valid_ssh_conn(server):
    cli = client.SSHClient()
    cli.set_missing_host_key_policy(client.AutoAddPolicy())
    try:
        sshCnx = cli.connect('bongo.coredial.com', username='jfifer', password='*****', look_for_keys=False)
    except IOError as err:
       return jsonify("false")
    except paramiko.PasswordRequiredException as err:
       return jsonify("false")
    except paramiko.AuthenticationConnection as err:
       return jsonify("false")
    return jsonify("true")

  def valid_fs_server(server):
    return true

  def valid_context(src, dst):
    return true

  def update_status(status_id):
    return true
