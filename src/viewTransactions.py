import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

table=None

def viewtransactions(acc_id):  
    db=db_connect()
    cursor=db.cursor()

    sql=f"select transaction_id, a.id, acc_name, t.money, tran_type, tran_date, tran_time \
        from transactions as t inner join accounts_details as a \
        on t.id=a.id \
        where a.id='{acc_id}';"
    cursor.execute(sql)
    results=cursor.fetchall()

    print(results)
    db.close()
    return results

def renderTransactions(root,messageLabel, result):
    # Showing account details
    data=viewtransactions(result)

    # clearing previous table
    global table
    if table:
        table.destroy()

    # rendering table
    if len(data)>0:
        df = pd.DataFrame(data)
        print(df)
        messageLabel.config(text="")

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
        messageLabel.config(text="Wrong Acc no. or No transactions fro this Account.")

def viewTransactions(root,is_user):

    # heading
    tk.Label(
        root,
        text="Transaction Details:",
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
    if is_user==True:
        label_otp= tk.Label(
            root,
            text="Enter OTP: ",
            bg="lightblue",
            font=("Arial", 12)
        )
        label_otp.pack(pady=(10, 0))
        entry_otp = tk.Entry(root, width=30)
        entry_otp.pack(pady=(5,10))

    # show message
    messageLabel=tk.Label(
            root,
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        )

    # Button- Show results
    btn_showResult= tk.Button(
        root,
        text="Show Transaction",
        command=lambda:renderTransactions(root, messageLabel, entry_accNo.get())
    )
    btn_showResult.pack(pady=20)

    messageLabel.pack(pady=10)

# viewTransactions(root, True)
# root.mainloop()