import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def view_all_transactions():
    
    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT * FROM transactions;"
    cursor.execute(sql)
    results=cursor.fetchall()

    # print(results)
    db.close()
    return results

def viewAllTransactions(root):

    # heading
    tk.Label(
        root,
        text="All Transaction Details",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # making dataframe from the result
    data=view_all_transactions()
    df = pd.DataFrame(data)
    # print(df)

    tree = ttk.Treeview(root, columns=list(df.columns), show="headings", height=min(len(df), 10))

    # Create column headings
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Insert rows
    for row in df.itertuples(index=False):
        tree.insert("", tk.END, values=row)

    tree.pack()
    

# viewAllTransactions(root)
# root.mainloop()