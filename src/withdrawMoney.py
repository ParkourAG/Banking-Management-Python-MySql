import tkinter as tk
from db_config import db_connect
from db_operations import isExist
from db_operations import checkUserPassword

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def transaction_debit_update(messageLabel, acc_id, ammount, password):
    db=db_connect()

    if isExist(db, acc_id):
        cursor=db.cursor()

        # check if password is correct
        if checkUserPassword(db, acc_id, password):
            try:
                sql1=f"select money from accounts_details where id={acc_id}"
                cursor.execute(sql1)
                moneyInAcc= cursor.fetchone()
                moneyInAcc=float(moneyInAcc[0])
                ammount=float(ammount)
                # print(moneyInAcc)
                # print(type(moneyInAcc))

                # check if account has sufficient money
                if (moneyInAcc-(ammount+1)) > 0:
                    try:
                        sql3=f"insert into transactions (id, money, tran_type) \
                            values({acc_id},'{ammount}','withdraw');"
                        cursor.execute(sql3)

                        sql2=f"UPDATE accounts_details \
                                SET money = money - {ammount} \
                                WHERE id = {acc_id};"
                        cursor.execute(sql2)

                        db.commit()   
                        messageLabel.config(text="Transaction Successfull. Please visit Again.")
                    except Exception as e:
                        print(f"Error: {e}")
                        messageLabel.config(text="Enter Ammount Correctly.")
                    finally:                 
                        db.close()
                
                else:   
                    messageLabel.config(text="Insufficient Money in Account")
                    db.close()

            except Exception as e:
                print(f"Error: {e}")
                messageLabel.config(text="Wrong Credentials. Please enter again.")
        else:
            messageLabel.config(text="Wrong Password.")

    else:
        messageLabel.config(text="Enter Account number Correctly.")
        db.close()


def withdrawMoney(root):

    # heading
    tk.Label(
        root,
        text="Withdraw Money:",
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

    # Enter Password 
    tk.Label(
        root,
        text="Enter Password : ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack(pady=(5, 0))
    password=tk.Entry(root, width=30)
    password.pack(pady=(5,10))

    # show message
    messageLabel=tk.Label(
            root,
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        )

    # button: Withdraw money
    tk.Button(
        root,
        text="Withdraw Money",
        command=lambda:transaction_debit_update(messageLabel, acc_entry.get(), money.get(), password.get())
    ).pack(pady=10)

    messageLabel.pack(pady=10)

# withdrawMoney(root)
# root.mainloop()