import tkinter as tk
import pymysql as pms

def db_connect():
   return pms.connect(
      user="root",
      password="password",
      host="localhost",
      database="bank_database"
   )

def transaction_credit_update(acc_id, ammount):
    db=db_connect()
    cursor=db.cursor()
    sql=f"insert into transactions (id, money, tran_type) \
          values({acc_id},'{ammount}','credit');"
    cursor.execute(sql)
    db.commit()
    
    db.close()

def depositeMoney(root):

    # heading
    tk.Label(
        root,
        text="Deposite Money:",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter Account Id
    tk.Label(
        root,
        text="Enter Account Number: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack(pady=(40, 0))
    acc_entry=tk.Entry(root, width=30)
    acc_entry.pack(pady=(5,20))

    # Enter Ammount
    tk.Label(
        root,
        text="Enter Ammount: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack(pady=(5, 0))
    money=tk.Entry(root, width=30)
    money.pack(pady=(5,10))

    # button: Deposite money
    tk.Button(
        root,
        text="Deposite Money",
        command=lambda:transaction_credit_update(acc_entry.get(), money.get())
    ).pack(pady=10)
