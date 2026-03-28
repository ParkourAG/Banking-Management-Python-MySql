from db_config import db_connect

def transactions_record_show():
    acc_id= input("Enter your Account Id: ")

    db=db_connect()
    cursor=db.cursor()

    sql=f"select transaction_id, a.id, acc_name, t.money, tran_type, tran_date, tran_time \
        from transactions as t inner join accounts_details as a \
        on t.id=a.id \
        where a.id='{acc_id}';"
    cursor.execute(sql)
    results= cursor.fetchall()

    for row in results:
        print(f"\ntransaction id   = {row[0]}")
        print(f"account id       = {row[1]}")
        print(f"name             = {row[2]}")
        print(f"money            = {row[3]}")
        print(f"transaction type = {row[4]}")
        print(f"transaction date = {row[5]}")
        print(f"transaction time = {row[6]}\n")
    
    db.close()

# transactions_record_show()