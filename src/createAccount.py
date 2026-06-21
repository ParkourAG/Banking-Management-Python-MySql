import tkinter as tk
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def create_account(name, ph, email):
    try:
        db=db_connect()
        cursor=db.cursor()
        sql1= f"INSERT INTO accounts_details(acc_name, ph_no, email) values('{name}', '{ph}', '{email}');"

        cursor.execute(sql1)
        db.commit()

        print("Your is created successfully.\n")
        print("Check your Account id in Search menu.")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()

    finally:    
        db.close()

def createAccount(root):

    # heading
    tk.Label(
        root,
        text="Create Your Account",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter Name
    label_username= tk.Label(
        root,
        text="Enter Name: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_username.pack(pady=(40, 0))

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=(5,30))

    # Enter Phone no
    label_phone= tk.Label(
        root,
        text="Enter phone no: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_phone.pack()

    entry_phone = tk.Entry(root, width=30)
    entry_phone.pack(pady=(5,30))

    # Enter Email
    label_email= tk.Label(
        root,
        text="Enter Email: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_email.pack()

    entry_email = tk.Entry(root, width=30)
    entry_email.pack(pady=(5,30))

    # Enter Password
    label_password= tk.Label(
        root,
        text="Enter Password: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_password.pack()

    entry_password = tk.Entry(root, width=30)
    entry_password.pack(pady=(5,30))

    # Enter OTP
    label_otp= tk.Label(
        root,
        text="Enter OTP: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_otp.pack()

    entry_otp = tk.Entry(root, width=30)
    entry_otp.pack(pady=(5,30))

    # Button Create account
    btn_createAccount= tk.Button(
        root,
        text="Create Account",
        command= lambda:create_account(entry_username.get(), entry_phone.get(), entry_email.get())
    )
    btn_createAccount.pack(pady=20)

    # 


# createAccount(root)
# root.mainloop()