import tkinter as tk
from db_config import db_connect
from db_operations import isExist

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def delete_account(messageLabel, acc_id):
    try:
        db= db_connect()

        if isExist(db, acc_id):
            cursor=db.cursor()
            sql= f"UPDATE accounts_details \
                            SET acc_status = 'inactive' \
                            WHERE id = {acc_id};"
            cursor.execute(sql)
            db.commit()

            # show message
            messageLabel.config(text=f"Acc no:{acc_id} is deleted successfully.")

        else:
            messageLabel.config(text=f"Acc no:{acc_id} dosent exist.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def deleteAccount(root):

    # heading
    tk.Label(
        root,
        text="Delete Account",
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

    # Button: Delete Account
    tk.Button(
        root,
        text="Delete Account",
        command= lambda:delete_account(messageLabel, entry_id.get())
    ).pack(pady=10)

    messageLabel.pack(pady=10)

# deleteAccount(root)
# root.mainloop()