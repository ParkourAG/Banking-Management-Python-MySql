import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

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

def renderTransactions(root,result):
    # Showing account details
    data=viewtransactions(result)

    if len(data)>1:
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
    else:
        tk.Label(
            root,
            text="Wrong Account no or, No transaction Data.",
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        ).pack(pady=10)


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

    # Button- Show results
    btn_showResult= tk.Button(
        root,
        text="Show Transaction",
        command=lambda:renderTransactions(root, entry_accNo.get())
    )
    btn_showResult.pack(pady=20)


# showAccountInfo(root)
# root.mainloop()