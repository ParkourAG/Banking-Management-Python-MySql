import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

def view_all_admin_account():
    
    db=db_connect()
    cursor=db.cursor()

    sql=f"SELECT emp_id, emp_name, ph_no, email, join_date, leave_date, admin_position, admin_status FROM employees;"
    cursor.execute(sql)
    results=cursor.fetchall()

    # print(results)
    db.close()
    return results
   
def viewAllAdmin(root):
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
        text="Employee Directory",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= TITLE =================
    tk.Label(
        root,
        text="Administrator Accounts",
        font=("Segoe UI", 20, "bold"),
        bg="#edf2f7",
        fg="#0f4c81"
    ).pack(pady=(25, 15))

    # ================= TABLE FRAME =================
    # Fetch Data
    data = view_all_admin_account()
    columns = [
                "Employee ID",
                "Employee Name",
                "Phone Number",
                "Email Address",
                "Joining Date",
                "Leaving Date",
                "Employee Position",
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
