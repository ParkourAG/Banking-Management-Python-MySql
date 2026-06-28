import pymysql as pms

def db_connect():
   return pms.connect(
      user="root",
      password="",
      host="localhost",
      database=""
   )

db_connect()