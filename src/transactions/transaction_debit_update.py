from db_config import db_connect

def transaction_debit_update(acc_id, ammount):

    db=db_connect()
    cursor=db.cursor()

    sql=f"insert into transactions (id, money, tran_type) \
          values({acc_id},'{ammount}','debit');"
    cursor.execute(sql)
    db.commit()
    
    db.close()

# transaction_debit_update(2,900)