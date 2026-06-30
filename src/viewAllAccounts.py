import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect


def view_all_accounts():
    
    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT id, acc_name, ph_no, email, money, create_date, create_time, acc_status FROM accounts_details;"
    cursor.execute(sql)
    results=cursor.fetchall()

    # print(results)
    db.close()
    return results
  
def viewAllAccounts(root):
    root.configure(bg="#edf2f7")

    # ================= HEADER =================
    header = tk.Frame(root, bg="#0f4c81", height=100)
    header.pack(fill="x")

    tk.Label(
        header,
        text="BMS BANK",
        font=("Segoe UI", 26, "bold"),
        bg="#0f4c81",
        fg="white"
    ).pack(pady=(18, 0))

    tk.Label(
        header,
        text="All Customer Accounts",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= TITLE =================
    tk.Label(
        root,
        text="Customer Account Details",
        font=("Segoe UI", 20, "bold"),
        bg="#edf2f7",
        fg="#0f4c81"
    ).pack(pady=(25, 15))


    # ================= VIEW TABLE =================
    # Fetch Data
    data = view_all_accounts()
    columns = [
                "Account No.",
                "Account Holder",
                "Phone Number",
                "Email Address",
                "Balance (₹)",
                "Created Date",
                "Created Time",
                "Status"
            ]

    df = pd.DataFrame(data, columns=columns)

    table = ttk.Treeview(
                root,
                columns=list(df.columns),
                show="headings",
                height=min(len(df), 10)
            )

    # Create headings
    for col in df.columns:
                table.heading(col, text=col)
                table.column(col, width=150, anchor="center")

            # Insert rows
    for row in df.itertuples(index=False):
                table.insert("", tk.END, values=row)

    table.pack()
    

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Officer Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=15)
    

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Administrator Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=15)
