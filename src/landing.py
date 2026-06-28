import tkinter as tk
from userinterface import userInterface
from adminInterface import adminInterface
from createAccount import createAccount
from officerInterface import officerInterface
from db_config import db_connect


# root = tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.resizable(False, False)
# root.configure(bg="lightblue")


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

def checkPassword(db, emp_id, password):
    cursor=db.cursor()
    sql= f"select emp_password, admin_status, admin_position from employees where emp_id={emp_id};"
    cursor.execute(sql)
    result= cursor.fetchone()
    if result==None:
        return None
    resultPassword=str(result[0])
    admin_status=str(result[1])
    admin_position=str(result[2])
    if resultPassword==password:
         return (True, admin_status, admin_position)
    else:
         return (False, admin_status, admin_position)

def landing(root):
    clear_root(root)

    tk.Label(
        root,
        text="Welcome to BMS Banking System",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    tk.Label(
        root,
        text="Login as:",
        font=("Arial", 15, "bold"),
        bg="lightblue",
        fg="white"
    ).pack()

    tk.Button(
        root,
        text="Admin",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:adminLogin(root)
    ).pack(pady=20)

    tk.Button(
        root,
        text="User",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:userLogin(root)
    ).pack()

      # create account
    createAccount= tk.Button(
        root,
        text="Create Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:createAccountPage(root)
    )
    createAccount.pack(pady=10)

def officerInterfacePage(root):
    clear_root(root)
    officerInterface(root)

def adminLogin(root):
    clear_root(root)

    tk.Label(
        root,
        text="Welcome to BMS Banking System",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Heading 
    tk.Label(
        root,
        text="Admin Login",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=30)

    # Enter Admin Id
    tk.Label(
        root,
        text="Enter Admin Id",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()

    admin_id = tk.Entry(root, width=30)
    admin_id.pack(pady=5)

    # Enter Admin Password
    tk.Label(
        root,
        text="Enter Password",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()

    admin_password = tk.Entry(root, show="*", width=30)
    admin_password.pack(pady=5)

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    # Login Button
    tk.Button(
        root,
        text="Login",
        bg="#0272ea",
        fg="white",
        command=lambda:checkAdminStatus(root, messageLabel, admin_id.get(), admin_password.get())
    ).pack(pady=20)

    # Back Button
    tk.Button(
        root,
        text="Back",
        command=lambda:landing(root)
    ).pack()

    messageLabel.pack(pady=10)

def userLogin(root):
    clear_root(root)
    userPage(root)
    
def checkAdminStatus(root, messageLabel, emp_id, password):
    db= db_connect()
    cursor=db.cursor()

    try:
        isPasswordCorrect= checkPassword(db, emp_id, password)[0]
        adminStatus= checkPassword(db, emp_id, password)[1]
        adminPosition= checkPassword(db, emp_id, password)[2]
        messageLabel.config(text="")

        # if Wrong password
        if isPasswordCorrect:
            if adminStatus == "active":
                if adminPosition== "po":
                    # If Login is Successfull
                    clear_root(root)
                    adminInterface(root)
                elif adminPosition=="officer":
                    clear_root(root)
                    officerInterfacePage(root)
            else:
                messageLabel.config(text="Account is either DELETED or BLOCKED. Please Contact to Officer.")
        else:
            messageLabel.config(text="Wrong Password! Please Try again")
    
    except Exception as e:
        # print(f"Error: {e}")
        messageLabel.config(text="Please Enter Admin id Correctly.")
    finally:
        db.close()

    
def userPage(root):
    clear_root(root)
    userInterface(root)

def createAccountPage(root):
    clear_root(root)
    createAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:landing(root)
    ).pack()


# landing()
# root.mainloop()

# db=db_connect()
# print(checkPassword(db, 15, "rahul1234"))