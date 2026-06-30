from db_config import db_connect
db=db_connect()

def isExist(db, acc_id):
    cursor=db.cursor()
    sql= f"select id from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    # check if account exists or not
    if result== None:
        return False
    else:
        return True

def isAdminExist(db, admin_id):
    cursor=db.cursor()
    sql= f"select emp_id from employees where emp_id={admin_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    # check if account exists or not
    if result== None:
        return False
    else:
        return True

def isAdminBlocked(db, admin_id): 
    cursor=db.cursor()
    sql= f"select admin_status from employees where emp_id={admin_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="blocked":
            return True
    else:
        print(f"Acc no:{admin_id} is not block.")
        return False

def isAdminInactive(db, admin_id): 
    cursor=db.cursor()
    sql= f"select admin_status from employees where emp_id={admin_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="inactive":
            return True
    else:
        print(f"Acc no:{admin_id} is active.")
        return False

def ifExistPh(db, ph):
    cursor=db.cursor()
    sql= f"select id from accounts_details where ph_no={ph};"
    cursor.execute(sql)
    result= cursor.fetchone()

    # check if account exists or not
    if result== None:
        return False
    else:
        return True
     
def ifAdminExistPh(db, ph):
    cursor=db.cursor()
    sql= f"select emp_id from employees where ph_no={ph};"
    cursor.execute(sql)
    result= cursor.fetchone()

    # check if account exists or not
    if result== None:
        return False
    else:
        return True

def isBlocked(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="blocked":
            return True
    else:
        print(f"Acc no:{acc_id} is not block.")
        return False

def isInactive(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="inactive":
            return True
    else:
        print(f"Acc no:{acc_id} is not inactive")
        return False
     
def isActive(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="active":
            return True
    else:
        print(f"Acc no:{acc_id} is not active.")
        return False

def isDeleted(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    if result[0]=="inactive":
            return True
    else:
        print(f"Acc no:{acc_id} is inactive.")
        return False

def checkUserPassword(db, user_id, password):
    cursor=db.cursor()
    sql= f"select user_password  from accounts_details where id={user_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    result=str(result[0])
    if result==password:
         return True
    else:
         return False
    
def checkAdminPassword(db, admin_id, password):
    cursor=db.cursor()
    sql= f"select emp_password  from employees where emp_id={admin_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    result=str(result[0])
    if result==password:
         return True
    else:
         return False
