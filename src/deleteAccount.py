import tkinter as tk
from db_config import db_connect
from db_operations import isExist


def delete_account(messageLabel, acc_id):
    try:
        db= db_connect()

        if isExist(db, acc_id):
            cursor=db.cursor()
            sql= f"UPDATE accounts_details \
                            SET acc_status = 'inactive' \
                            WHERE id = {acc_id};"
            cursor.execute(sql)
            db.commit()

            # show message
            messageLabel.config(text=f"Acc no:{acc_id} is deleted successfully.")

        else:
            messageLabel.config(text=f"Acc no:{acc_id} dosent exist.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def deleteAccount(root):
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
        text="Delete Customer Account",
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
        text="Delete User Account",
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

    entry_id = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_id.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Delete Button --------
    tk.Button(
        card,
        text="Delete Account",
        font=("Segoe UI", 11, "bold"),
        bg="#dc2626",
        fg="white",
        activebackground="#b91c1c",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: delete_account(
            messageLabel,
            entry_id.get()
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
