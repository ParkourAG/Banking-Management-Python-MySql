import tkinter as tk
from db_config import db_connect
from db_operations import isExist

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def transaction_credit_update(messageLabel, acc_id, ammount):
    db=db_connect()

    if isExist(db, acc_id):
        cursor=db.cursor()

        try:
            acc_id= int(acc_id)
            ammount= float(ammount)

            # update ammount
            sql1=f"""UPDATE accounts_details 
                    SET money = money + "{ammount}" 
                    WHERE id = "{acc_id}";"""
            cursor.execute(sql1)
            
            # update transaction data
            sql2=f"insert into transactions (id, money, tran_type) \
                    values('{acc_id}','{ammount}','deposit');"
            cursor.execute(sql2)
            db.commit()
            db.close()
            messageLabel.config(text="Transaction Successfull. Please visit Again.")
        except Exception as e:
            messageLabel.config(text="Wrong Credentials. Please enter again.")
            print(f"Error: {e}")
    else:
        messageLabel.config(text="Wrong Account Id.")

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

    # show message
    messageLabel=tk.Label(
            root,
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        )

    # button: Deposite money
    tk.Button(
        root,
        text="Deposite Money",
        command=lambda:transaction_credit_update(messageLabel, acc_entry.get(), money.get())
    ).pack(pady=10)

    messageLabel.pack(pady=10)


# depositeMoney(root)
# root.mainloop()