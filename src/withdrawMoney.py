import tkinter as tk
from db_config import db_connect
from db_operations import isExist
from db_operations import checkUserPassword


def transaction_debit_update(messageLabel, acc_id, ammount, password):
    db=db_connect()

    if isExist(db, acc_id):
        cursor=db.cursor()

        # check if password is correct
        if checkUserPassword(db, acc_id, password):
            try:
                sql1=f"select money from accounts_details where id={acc_id}"
                cursor.execute(sql1)
                moneyInAcc= cursor.fetchone()
                moneyInAcc=float(moneyInAcc[0])
                ammount=float(ammount)
                # print(moneyInAcc)
                # print(type(moneyInAcc))

                # check if account has sufficient money
                if (moneyInAcc-(ammount+1)) > 0:
                    try:
                        sql3=f"insert into transactions (id, money, tran_type) \
                            values({acc_id},'{ammount}','withdraw');"
                        cursor.execute(sql3)

                        sql2=f"UPDATE accounts_details \
                                SET money = money - {ammount} \
                                WHERE id = {acc_id};"
                        cursor.execute(sql2)

                        db.commit()   
                        messageLabel.config(text="Transaction Successfull. Please visit Again.")
                    except Exception as e:
                        print(f"Error: {e}")
                        messageLabel.config(text="Enter Ammount Correctly.")
                    finally:                 
                        db.close()
                
                else:   
                    messageLabel.config(text="Insufficient Money in Account")
                    db.close()

            except Exception as e:
                print(f"Error: {e}")
                messageLabel.config(text="Wrong Credentials. Please enter again.")
        else:
            messageLabel.config(text="Wrong Password.")

    else:
        messageLabel.config(text="Enter Account number Correctly.")
        db.close()

def withdrawMoney(root):
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
        text="Withdraw Funds",
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
        text="Withdraw Money",
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
        text="Amount",
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
    money.pack(ipady=5, pady=(5, 15))

    # -------- Password --------
    tk.Label(
        card,
        text="Password",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    password = tk.Entry(
        card,
        width=35,
        show="*",
        font=("Segoe UI", 11)
    )
    password.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Withdraw Button --------
    tk.Button(
        card,
        text="Withdraw Money",
        font=("Segoe UI", 11, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: transaction_debit_update(
            messageLabel,
            acc_entry.get(),
            money.get(),
            password.get()
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
