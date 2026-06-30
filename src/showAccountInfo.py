import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect
from db_operations import checkUserPassword


table=None

def accountInfo(acc_id, password):
    db=db_connect()
    if checkUserPassword(db, acc_id, password):
        cursor=db.cursor()

        sql=f"SELECT id, acc_name, ph_no, email, money, create_date, create_time, acc_status FROM accounts_details WHERE id='{acc_id}';"
        cursor.execute(sql)
        results=cursor.fetchall()
        db.close()
        return results
    else:
         return None

def renderAccountInfo(root,messageLabel, acc_id, password):
        data=accountInfo(acc_id, password)
        messageLabel.config(text="")

        # clearing previous table
        global table
        if table:
            table.destroy()

        # if the password is Correct
        if data!=None:
            df = pd.DataFrame(data)

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
             messageLabel.config(text="Please Enter Account no and Password correctly.")
  
def showAccountInfo(root):
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
        text="View Account Information",
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
    card.pack(pady=50)

    tk.Label(
        card,
        text="Account Details",
        font=("Segoe UI", 20, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack(pady=(0, 25))

    # -------- Account Number --------
    tk.Label(
        card,
        text="Account Number",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_accNo = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_accNo.pack(ipady=5, pady=(5, 15))

    # -------- Password --------
    tk.Label(
        card,
        text="Password",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_password = tk.Entry(
        card,
        width=35,
        show="*",
        font=("Segoe UI", 11)
    )
    entry_password.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Show Button --------
    tk.Button(
        card,
        text="Show Account Information",
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
            entry_accNo.get(),
            entry_password.get()
        )
    ).pack()

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Secure Banking • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
