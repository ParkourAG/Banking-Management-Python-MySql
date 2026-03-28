from db_config import db_connect

def credit_cash(acc_id, ammount):
    # acc_id=input("Enter your Account Id: ")
    # ammount=input("Enter Ammount to credit: ")

    db=db_connect()
    cursor=db.cursor()

    sql1= f"UPDATE accounts_details SET money=money+{ammount} WHERE id='{acc_id}';"
    sql2=f"SELECT * FROM accounts_details WHERE id='{acc_id}';"
    cursor.execute(sql1)
    db.commit()
    cursor.execute(sql2)
    results=cursor.fetchall()

    for row in results:
        print("-------current status-------")
        print(f"\nAcc id  : {row[0]}")
        print(f"Name    : {row[1]}")
        print(f"Phone no: {row[2]}")
        print(f"Email   : {row[3]}")
        print(f"Money   : {row[4]}")

    # print(results)
    db.close()

# credit_cash()