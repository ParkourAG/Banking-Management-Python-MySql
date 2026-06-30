import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect


table=None

def search_account(acc_id, name, phone, email):
    try:
        db=db_connect()
        cursor=db.cursor()
        sql=f"SELECT id, acc_name, ph_no, email, money, create_date, create_time, acc_status FROM accounts_details WHERE id='{acc_id}' OR acc_name='{name}' OR ph_no='{phone}' OR email='{email}';"
        cursor.execute(sql)
        results=cursor.fetchall()

        # print(results)
        return results
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
        
def renderAccountInfo(root, messageLabel, acc_id, name, phone, email):
        data=search_account(acc_id, name, phone, email)

        # clearing previous table
        global table
        if table:
            table.destroy()

        # print(f"Data: {data}")

        # if result is not empty
        if len(data)>0:
            messageLabel.config(text="")
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
        else:
            messageLabel.config(text="No Account found")

def searchAccount(root):
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
        text="Search Customer Account",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= CARD =================
    card = tk.Frame(
        root,
        bg="white",
        bd=1,
        relief="solid",
        padx=40,
        pady=35
    )
    card.pack(pady=30)

    tk.Label(
        card,
        text="Search User Account",
        font=("Segoe UI", 20, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack(pady=(0, 25))

    # -------- Name --------
    tk.Label(
        card,
        text="Customer Name",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_username = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_username.pack(ipady=5, pady=(5, 15))

    # -------- Phone --------
    tk.Label(
        card,
        text="Phone Number",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_phone = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_phone.pack(ipady=5, pady=(5, 15))

    # -------- Account Number --------
    tk.Label(
        card,
        text="Account Number",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_id = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_id.pack(ipady=5, pady=(5, 15))

    # -------- Email --------
    tk.Label(
        card,
        text="Email Address",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_email = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_email.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Search Button --------
    tk.Button(
        card,
        text="Search Account",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: renderAccountInfo(
            root,
            messageLabel,
            entry_id.get(),
            entry_username.get(),
            entry_phone.get(),
            entry_email.get()
        )
    ).pack()

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Administrator Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
