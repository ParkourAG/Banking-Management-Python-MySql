import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def search_account():                                           # give id, delete the name and phone, rewrite the sql querry
    # name=input("Enter your Name: ")
    # phone=input("Enter your Phone No: ")
    name="anubrata"
    phone="789456123"

    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT * FROM accounts_details WHERE acc_name='{name}' AND ph_no='{phone}';"
    cursor.execute(sql)
    results=cursor.fetchall()

    # for row in results:
    #     print(f"\nAcc id  : {row[0]}")
    #     print(f"Name    : {row[1]}")
    #     print(f"Phone no: {row[2]}")
    #     print(f"Email   : {row[3]}")
    #     print(f"Money   : {row[4]}")

    print(results)
    db.close()
    return results

def showAccountInfo(root):


    # heading
    tk.Label(
        root,
        text="Account Details:",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # # Enter Account Id
    # tk.Label(
    #     root,
    #     text="Enter Account Number",
    #     bg="lightblue",
    #     font=("Arial", 12)
    # ).pack(pady=(40, 0))
    # tk.Entry(root, width=30).pack(pady=(5,20))

    # Showing account details

    data=search_account()
    df = pd.DataFrame(data)
    print(df)

    # root = tk.Tk()
    # root.title("DataFrame Table")

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