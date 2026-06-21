import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def accountInfo(acc_id):
    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT * FROM accounts_details WHERE id='{acc_id}';"
    cursor.execute(sql)
    results=cursor.fetchall()

    print(results)
    db.close()
    return results

def renderAccountInfo(root, acc_id):
        data=accountInfo(acc_id)
        df = pd.DataFrame(data)
        print(df)

        tree = ttk.Treeview(root, columns=list(df.columns), show="headings", height=min(len(df), 10))

        # Create column headings
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Insert rows
        for row in df.itertuples(index=False):
            tree.insert("", tk.END, values=row)

        tree.pack()

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

    #Enter OTP:
    label_otp= tk.Label(
        root,
        text="Enter OTP: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_otp.pack(pady=(10, 0))
    entry_otp = tk.Entry(root, width=30)
    entry_otp.pack(pady=(5,10))

    # Button- Show results
    btn_showResult= tk.Button(
        root,
        text="Show Account Info",
        command=lambda:renderAccountInfo(root, entry_accNo.get())
    )
    btn_showResult.pack(pady=20)
    

# showAccountInfo(root)
# root.mainloop()