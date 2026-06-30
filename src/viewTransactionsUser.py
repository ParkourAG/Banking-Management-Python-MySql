import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect


table=None

def viewtransactions(acc_id, password):  
    db=db_connect()
    cursor=db.cursor()
    try:

        sqlPassword= f"select user_password from accounts_details \
                       where id='{acc_id}'"
        cursor.execute(sqlPassword)
        getPassword=cursor.fetchone()
        getPassword= getPassword[0]
        # print(f"getPassword:{getPassword}, password:{password}")

        # if password is correct:
        if password==getPassword:
            sql=f"select transaction_id, a.id, acc_name, t.money, tran_type, tran_date, tran_time \
                from transactions as t inner join accounts_details as a \
                on t.id=a.id \
                where a.id='{acc_id}';"
            cursor.execute(sql)
            results=cursor.fetchall()

            # print(results)
            db.close()
            return results
        else:
            return None
        
    except Exception as e:
        print(f"viewtransactions Error: {e}")

def renderTransactions(root,messageLabel, acc_id, password):
    # Showing account details
    data=viewtransactions(acc_id, password)

    # clearing previous table
    global table
    if table:
        table.destroy()

    if data!=None:
        # rendering table
        if len(data)>0:
            columns = [
                        "Transaction ID",
                        "Account Number",
                        "Account Holder",
                        "Amount (₹)",
                        "Transaction Type",
                        "Date",
                        "Time"
                        ]

            df = pd.DataFrame(data, columns=columns)

            messageLabel.config(text="")

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
            messageLabel.config(text="Wrong Acc no. or No transactions fro this Account.")
    else:
        messageLabel.config(text="Incorrect password.")

def viewTransactions(root, is_user):
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

    # ================= CARD =================
    card = tk.Frame(
        root,
        bg="white",
        bd=1,
        relief="solid",
        padx=40,
        pady=35
    )
    card.pack(pady=40)

    tk.Label(
        card,
        text="View Transactions",
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
    if is_user == True:
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
            font=("Segoe UI", 11)
        )
        entry_password.pack(ipady=5, pady=(5, 20))

        # check for password


    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Button --------
    tk.Button(
        card,
        text="View Transactions",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: renderTransactions(
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
