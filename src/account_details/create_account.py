from db_config import db_connect

def create_account():
    name=input("Enter your name: ")
    phoneNo=input("Enter your phone no: ")
    email=input("Enter your Email: ")

    db=db_connect()
    cursor=db.cursor()
    sql1= f"INSERT INTO accounts_details(acc_name, ph_no, email) values('{name}', '{phoneNo}', '{email}');"

    cursor.execute(sql1)
    db.commit()

    print("Your is created successfully.\n")
    print("Check your Account id in Search menu.")
    db.close()

# create_account()