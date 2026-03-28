from db_config import db_connect

def transaction_credit_update(acc_id, ammount):

    db=db_connect()
    cursor=db.cursor()

    sql=f"insert into transactions (id, money, tran_type) \
          values({acc_id},'{ammount}','credit');"
    cursor.execute(sql)
    db.commit()
    
    db.close()

# transaction_credit_update(3,2000)