import tkinter as tk
from db_config import db_connect
from db_operations import isExist

def transaction_credit_update(messageLabel, acc_id, ammount):
    db=db_connect()

    if isExist(db, acc_id):
        cursor=db.cursor()

        try:
            acc_id= int(acc_id)
            ammount= float(ammount)

            # update ammount
            sql1=f"""UPDATE accounts_details 
                    SET money = money + "{ammount}" 
                    WHERE id = "{acc_id}";"""
            cursor.execute(sql1)
            
            # update transaction data
            sql2=f"insert into transactions (id, money, tran_type) \
                    values('{acc_id}','{ammount}','deposit');"
            cursor.execute(sql2)
            db.commit()
            db.close()
            messageLabel.config(text="Transaction Successfull. Please visit Again.")
        except Exception as e:
            messageLabel.config(text="Wrong Credentials. Please enter again.")
            print(f"Error: {e}")
    else:
        messageLabel.config(text="Wrong Account Id.")

def depositeMoney(root):
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
        text="Deposit Money",
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
        text="Deposit Money",
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

    acc_entry = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    acc_entry.pack(ipady=5, pady=(5, 15))

    # -------- Amount --------
    tk.Label(
        card,
        text="Deposit Amount",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    money = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    money.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Deposit Button --------
    tk.Button(
        card,
        text="Deposit Money",
        font=("Segoe UI", 11, "bold"),
        bg="#16a34a",
        fg="white",
        activebackground="#15803d",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: transaction_credit_update(
            messageLabel,
            acc_entry.get(),
            money.get()
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
