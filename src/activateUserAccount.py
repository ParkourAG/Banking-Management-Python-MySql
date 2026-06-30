import tkinter as tk
from db_config import db_connect
from db_operations import isBlocked, isExist, isInactive


def activateUserAccount(messageLabel, acc_id, root):
    try:
        db= db_connect()

#  Check if account exists
        if isExist(db, acc_id):

            # check if account is already blocked
            if isBlocked(db, acc_id) or isInactive(db, acc_id)==True:
                cursor=db.cursor()
                print(1)
                sql= f"UPDATE accounts_details \
                        SET acc_status = 'active' \
                        WHERE id = '{acc_id}';"
                cursor.execute(sql)
                print(2)
                db.commit()

                # printing message
                messageLabel.config(text="Account is Re-activated successfully.")
            else:
                # printing message
                messageLabel.config(text="Account is already Active.")
        
        else:
            messageLabel.config(text="Account dosent exist. please type account number correctly.")
            

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def activateUserAcc(root):
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
        text="Reactivate Customer Account",
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
        text="Reactivate User Account",
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

    # -------- Activate Button --------
    tk.Button(
        card,
        text="Activate Account",
        font=("Segoe UI", 11, "bold"),
        bg="#16a34a",
        fg="white",
        activebackground="#15803d",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: activateUserAccount(
            messageLabel,
            entry_id.get(),
            root
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
