from db_config import db_connect
# db=db_connect()

def isExist(db, acc_id):
    cursor=db.cursor()
    sql= f"select id from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()

    # check if account exists or not
    if result== None:
        print(f"Acc no:{acc_id} dosent exist.")
        return False
    else:
        return True

def isBlocked(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    #  check if the account exists
    if isExist(db, acc_id):
        if result[0]=="blocked":
            return True
        else:
            print(f"Acc no:{acc_id} is not block.")
            return False
    else:
        print(f"Acc no:{acc_id} dosent exist.")

def isActive(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    #  check if the account exists
    if isExist(db, acc_id):
        if result[0]=="active":
            return True
        else:
            print(f"Acc no:{acc_id} is not active.")
            return False
    else:
        print(f"Acc no:{acc_id} dosent exist.")

def isDeleted(db, acc_id):
    cursor=db.cursor()
    sql= f"select acc_status from accounts_details where id={acc_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    #  check if the account exists
    if isExist(db, acc_id):
        if result[0]=="inactive":
            return True
        else:
            print(f"Acc no:{acc_id} is not inactive.")
            return False
    else:
        print(f"Acc no:{acc_id} dosent exist.")


# print(ifBlocked(db, 1))
# db.close()