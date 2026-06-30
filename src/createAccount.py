import tkinter as tk
from db_config import db_connect
from db_operations import ifExistPh


def create_account(messageLabel, name, ph, email, password):
    if (len(name)>0) and (len(ph)>0) and (len(email)>0)and (len(password)>0):
        try:
            db=db_connect()
            ph=int(ph)

            if ifExistPh(db, ph)==False:
                cursor=db.cursor()
                sql1= f"INSERT INTO accounts_details(acc_name, ph_no, email, user_password) values('{name}', '{ph}', '{email}', '{password}');"

                cursor.execute(sql1)
                db.commit()

                # show message
                messageLabel.config(text="Account created successfully.")
                
            else:
                # show message
                messageLabel.config(text="Phone no. is already in Use.") 

        except Exception as e:
            messageLabel.config(text="Enter Credentials Properly.") 
            print(f"Error: {e}")
            db.rollback()

        finally:    
            db.close()
    else:
        messageLabel.config(text="Enter Credentials Properly.") 

def createAccount(root):

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
        text="Open a New Bank Account",
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
        pady=30
    )
    card.pack(pady=35)

    tk.Label(
        card,
        text="Create Account",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack(pady=(0, 25))

    # -------- Name --------
    tk.Label(
        card,
        text="Full Name",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_username = tk.Entry(card, width=35, font=("Segoe UI", 11))
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

    entry_phone = tk.Entry(card, width=35, font=("Segoe UI", 11))
    entry_phone.pack(ipady=5, pady=(5, 15))

    # -------- Email --------
    tk.Label(
        card,
        text="Email Address",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_email = tk.Entry(card, width=35, font=("Segoe UI", 11))
    entry_email.pack(ipady=5, pady=(5, 15))

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
        show="*",
        width=35,
        font=("Segoe UI", 11)
    )
    entry_password.pack(ipady=5, pady=(5, 15))

    # -------- OTP --------
    tk.Label(
        card,
        text="OTP",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_otp = tk.Entry(card, width=35, font=("Segoe UI", 11))
    entry_otp.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        bg="white",
        fg="red",
        font=("Segoe UI", 10, "bold")
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Create Button --------
    tk.Button(
        card,
        text="Create Account",
        font=("Segoe UI", 11, "bold"),
        bg="#0f4c81",
        fg="white",
        activebackground="#1565a9",
        activeforeground="white",
        bd=0,
        width=22,
        height=2,
        cursor="hand2",
        command=lambda: create_account(
            messageLabel,
            entry_username.get(),
            entry_phone.get(),
            entry_email.get(),
            entry_password.get()
        )
    ).pack()

    # Footer
    tk.Label(
        root,
        text="Your information is protected with bank-grade security.",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
