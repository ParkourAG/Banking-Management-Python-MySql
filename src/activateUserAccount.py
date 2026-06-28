import tkinter as tk
from db_config import db_connect
from db_operations import isBlocked, isExist, isInactive

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def activateUserAccount(messageLabel, acc_id, root):
    try:
        db= db_connect()

#  Check if account exists
        if isExist(db, acc_id):

            # check if account is already blocked
            if isBlocked(db, acc_id) or isInactive(db, acc_id)==True:
                cursor=db.cursor()
                print(1)
                sql= f"UPDATE accounts_details \
                        SET acc_status = 'active' \
                        WHERE id = '{acc_id}';"
                cursor.execute(sql)
                print(2)
                db.commit()

                # printing message
                messageLabel.config(text="Account is Re-activated successfully.")
            else:
                # printing message
                messageLabel.config(text="Account is already Active.")
        
        else:
            messageLabel.config(text="Account dosent exist. please type account number correctly.")
            

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def activateUserAcc(root):

    # heading
    tk.Label(
        root,
        text="Re-activate User Account",
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
    entry_id=tk.Entry(root, width=30)
    entry_id.pack(pady=(5,20))

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    # Button: Activate Account
    tk.Button(
        root,
        text="Activate Account",
        command= lambda:activateUserAccount(messageLabel ,entry_id.get(), root)
    ).pack(pady=10)

    # Message
    messageLabel.pack(pady=10)

# blockAccount(root)
# root.mainloop()

# 