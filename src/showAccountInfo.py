import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect
from db_operations import checkUserPassword

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

table=None

def accountInfo(acc_id, password):
    db=db_connect()
    if checkUserPassword(db, acc_id, password):
        cursor=db.cursor()

        sql=f"SELECT * FROM accounts_details WHERE id='{acc_id}';"
        cursor.execute(sql)
        results=cursor.fetchall()
        db.close()
        return results
    else:
         return None

def renderAccountInfo(root,messageLabel, acc_id, password):
        data=accountInfo(acc_id, password)
        messageLabel.config(text="")

        # clearing previous table
        global table
        if table:
            table.destroy()

        # if the password is Correct
        if data!=None:
            df = pd.DataFrame(data)

            table = ttk.Treeview(root, columns=list(df.columns), show="headings", height=min(len(df), 10))

            # Create column headings
            for col in df.columns:
                table.heading(col, text=col)
                table.column(col, width=100)

            # Insert rows
            for row in df.itertuples(index=False):
                table.insert("", tk.END, values=row)

            table.pack()
        else:
             messageLabel.config(text="Please Enter Account no and Password correctly.")
             

def showAccountInfo(root):

    # heading
    tk.Label(
        root,
        text="Account Details:",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter account number
    label_accNo= tk.Label(
        root,
        text="Enter Account no: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_accNo.pack(pady=(40, 0))
    entry_accNo = tk.Entry(root, width=30)
    entry_accNo.pack(pady=(5,20))

    #Enter password:
    label_password= tk.Label(
        root,
        text="Enter Passwortd : ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_password.pack(pady=(10, 0))
    entry_password = tk.Entry(root, width=30)
    entry_password.pack(pady=(5,10))

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    # Button- Show results
    btn_showResult= tk.Button(
        root,
        text="Show Account Info",
        command=lambda:renderAccountInfo(root, messageLabel, entry_accNo.get(), entry_password.get())
    )
    btn_showResult.pack(pady=20)

    messageLabel.pack(pady=10)
    

# showAccountInfo(root)
# root.mainloop()