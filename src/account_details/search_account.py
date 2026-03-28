from db_config import db_connect

def search_account():
    name=input("Enter your Name: ")
    phone=input("Enter your Phone No: ")

    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT * FROM accounts_details WHERE acc_name='{name}' AND ph_no='{phone}';"
    cursor.execute(sql)
    results=cursor.fetchall()

    for row in results:
        print(f"\nAcc id  : {row[0]}")
        print(f"Name    : {row[1]}")
        print(f"Phone no: {row[2]}")
        print(f"Email   : {row[3]}")
        print(f"Money   : {row[4]}")

    print(results)
    db.close()

# search_account()