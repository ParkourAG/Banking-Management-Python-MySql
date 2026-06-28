import pymysql as pms

def db_connect():
   return pms.connect(
      user="root",
      password="",        ######## Enter Password ########
      host="localhost",
      database=""         ######## Emter Database Name ########
   )

db_connect()