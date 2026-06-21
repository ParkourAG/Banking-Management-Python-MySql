import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def viewtransactions():                                           # give id, delete the name and phone, rewrite the sql querry
    acc_id="13"

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

def viewTransactions(root):


    # heading
    tk.Label(
        root,
        text="Account Details:",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Showing account details
    data=viewtransactions()
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
    

# showAccountInfo(root)
# root.mainloop()