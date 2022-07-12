#!usr/bin/python3

import os
import psycopg2

def db_file_config():
        config_file = "\config\db.conf"
        return config_file

def db_config():
        config = {}
        fileconf = db_file_config()
        rfile = open(os.getcwd() + fileconf, "r")
        for line in rfile:
                line = line.replace("\n","")
                length = len(line)

                if (length != 0):
                        line = line.replace(" ", "")
                        (name, value) = line.split("=")
                        config[name] = value
        return config

def db_connect():
        config = db_config()

        host = config['host'].strip()
        db = config['database'].strip()
        port = config['port'].strip()
        user = config['user'].strip()
        pwd = config['password'].strip()

        while True:
                try:
                    conn = psycopg2.connect(host=host, database=db, user=user, password=pwd, port=port)
                except :
                    print("Oops!  Cannot Connect To PostgreSQL, Try again...")
                else:
                    break
        return conn