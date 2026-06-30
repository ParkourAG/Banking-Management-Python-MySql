import tkinter as tk
from db_config import db_connect
from db_operations import ifAdminExistPh


def create_admin(messageLabel1, messageLabel2 ,emp_name, ph_no, email, admin_position, password, root):
    try:
        db=db_connect()
        ph_no= int(ph_no)

        if ifAdminExistPh(db, ph_no)==False:
            if (len(emp_name)>0) and (len(ph_no)>0) and (len(email)>0)and (len(password)>0) and (admin_position== "officer" or admin_position== "po"):
                
                ph_no= int(ph_no)
                cursor=db.cursor()
                sql1= f"INSERT INTO employees (emp_name, ph_no, email, admin_position, emp_password) \
                        VALUES ('{emp_name}', '{ph_no}', '{email}', '{admin_position}', '{password}');"
                cursor.execute(sql1)
                db.commit()
                # printing message
                messageLabel1.config(text="Admin Account created successfully.")
                messageLabel2.config(text="Please search your Account using Phone no.")               
            else:
                messageLabel1.config(text="Please Enter Credentials Properly.")
        else:
            # printing message
            messageLabel1.config(text="Phone no is already in use.")
            messageLabel2.config(text="")

    except Exception as e:
        print(f"Error: {e}")
        messageLabel1.config(text="Please Enter Credentials Properly.")
        db.rollback()
    finally:    
        db.close()

def createAdminAccount(root):
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
        text="Create Administrator Account",
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
    card.pack(pady=30)

    tk.Label(
        card,
        text="Administrator Registration",
        font=("Segoe UI", 20, "bold"),
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

    entry_empName = tk.Entry(card, font=("Segoe UI", 11), width=35)
    entry_empName.pack(ipady=5, pady=(5, 15))

    # -------- Phone --------
    tk.Label(
        card,
        text="Phone Number",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_phone = tk.Entry(card, font=("Segoe UI", 11), width=35)
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

    entry_email = tk.Entry(card, font=("Segoe UI", 11), width=35)
    entry_email.pack(ipady=5, pady=(5, 15))

    # -------- Position --------
    tk.Label(
        card,
        text="Position (Officer / PO)",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_position = tk.Entry(card, font=("Segoe UI", 11), width=35)
    entry_position.pack(ipady=5, pady=(5, 15))

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
        font=("Segoe UI", 11),
        width=35
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

    entry_otp = tk.Entry(card, font=("Segoe UI", 11), width=35)
    entry_otp.pack(ipady=5, pady=(5, 20))

    # -------- Messages --------
    messageLabel1 = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel1.pack()

    messageLabel2 = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="#0f4c81"
    )
    messageLabel2.pack(pady=(5, 15))

    # -------- Create Button --------
    tk.Button(
        card,
        text="Create Administrator",
        font=("Segoe UI", 11, "bold"),
        bg="#16a34a",
        fg="white",
        activebackground="#15803d",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: create_admin(
            messageLabel1,
            messageLabel2,
            entry_empName.get(),
            entry_phone.get(),
            entry_email.get(),
            entry_position.get(),
            entry_password.get(),
            root
        )
    ).pack(pady=10)

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Officer Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
