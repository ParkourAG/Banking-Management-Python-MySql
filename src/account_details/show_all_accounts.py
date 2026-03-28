from db_config import db_connect

def all_accounts():

    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT * FROM accounts_details;"
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