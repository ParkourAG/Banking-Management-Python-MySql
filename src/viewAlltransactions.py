import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect


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
        text="Transaction History",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= TITLE =================
    tk.Label(
        root,
        text="All Transactions",
        font=("Segoe UI", 20, "bold"),
        bg="#edf2f7",
        fg="#0f4c81"
    ).pack(pady=(25, 15))

    
    # ================= VIEW TABLE =================
    # Fetch Data
    data = view_all_transactions()
    columns = [
                        "Transaction ID",
                        "Account Number",
                        "Amount (₹)",
                        "Transaction Type",
                        "Date",
                        "Time"
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
        text="Secure Banking • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=15)