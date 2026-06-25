import tkinter as tk
from db_config import db_connect
from db_operations import isBlocked
from db_operations import isExist

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def block_account(acc_id, root):
    try:
        db= db_connect()

#  Check if account exists
        if isExist(db, acc_id):

            # check if account is already blocked
            if isBlocked(db, acc_id)==False:
                cursor=db.cursor()
                sql= f"UPDATE accounts_details \
                        SET acc_status = 'blocked' \
                        WHERE id = {acc_id};"
                cursor.execute(sql)
                db.commit()

                # printing message
                tk.Label(
                    root,
                    text="Account is blocked successfully.",
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                ).pack(pady=10)
            else:
                # printing message
                tk.Label(
                    root,
                    text="Account is already blocked.",
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                ).pack(pady=10)
        
        else:
            tk.Label(
                    root,
                    text="Account dosent exist. Please type Account no correctly.",
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                ).pack(pady=10)
            

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def blockAccount(root):

    # heading
    tk.Label(
        root,
        text="Block Account",
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

    # Button: Block Account
    tk.Button(
        root,
        text="Block Account",
        command= lambda:block_account(entry_id.get(), root)
    ).pack(pady=10)

# blockAccount(root)
# root.mainloop()