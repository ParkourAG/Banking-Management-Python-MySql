import pymysql as pms

def db_connect():
   return pms.connect(
      user="root",
      password="password",
      host="localhost",
      database="bank_database"
   )

db_connect()