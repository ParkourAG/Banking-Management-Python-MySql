from db_config import db_connect

def delete_account():
    acc_id=input("Enter Account id to delete from bank database: ")
    db= db_connect
    cursor=db.cursor()

    sql= f"DELETE FROM accounts_details WHERE id='{acc_id}';"
    cursor.execute(sql)
    db.commit()

    print("your Account is deleted successfully..")
    db.close()

# delete_account()