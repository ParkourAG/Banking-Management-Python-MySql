import tkinter as tk
from db_config import db_connect
from db_operations import ifExistPh

root= tk.Tk()
root.title("BMS Bank")
root.geometry("700x800")
root.configure(bg="lightblue")
root.resizable(False,False)

def create_account(messageLabel, name, ph, email, password):
    if (len(name)>0) and (len(ph)>0) and (len(email)>0)and (len(password)>0):
        try:
            db=db_connect()
            ph=int(ph)
# hi
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

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    # Button Create account
    btn_createAccount= tk.Button(
        root,
        text="Create Account",
        command= lambda:create_account(messageLabel, entry_username.get(), entry_phone.get(), entry_email.get(), entry_password.get())
    )
    btn_createAccount.pack(pady=20)

    messageLabel.pack(pady=10)


createAccount(root)
root.mainloop()