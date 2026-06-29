import tkinter as tk
from db_config import db_connect
from db_operations import ifAdminExistPh

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

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

    # heading
    tk.Label(
        root,
        text="Create Admin Account",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=(20,10))

    # Enter Name
    label_empName= tk.Label(
        root,
        text="Enter Name: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_empName.pack(pady=(10, 0))

    entry_empName = tk.Entry(root, width=30)
    entry_empName.pack(pady=(5,30))

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

    # Enter Position
    label_position= tk.Label(
        root,
        text="Enter Position: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_position.pack()

    entry_position = tk.Entry(root, width=30)
    entry_position.pack(pady=(5,30))

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
        command= lambda:create_admin(messageLabel1, messageLabel2, entry_empName.get(), entry_phone.get(), entry_email.get(), entry_position.get(), entry_password.get(), root)
    )
    btn_createAccount.pack(pady=10)

    # Message
    messageLabel1=tk.Label(
            root,
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
    messageLabel1.pack(pady=10)
    messageLabel2=tk.Label(
            root,
            font=("Arial", 15, "bold"),
            bg="lightblue",
            fg="black"
        )
    messageLabel2.pack(pady=10)

# createAdminAccount(root)
# root.mainloop()