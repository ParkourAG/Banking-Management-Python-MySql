import tkinter as tk
from userinterface import userInterface
from adminInterface import adminInterface
from createAccount import createAccount
from officerInterface import officerInterface
from db_config import db_connect


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

    # Window background
    root.configure(bg="#edf2f7")

    # ================= HEADER =================
    header = tk.Frame(root, bg="#0f4c81", height=120)
    header.pack(fill="x")

    tk.Label(
        header,
        text="BMS BANK",
        font=("Segoe UI", 28, "bold"),
        bg="#0f4c81",
        fg="white"
    ).pack(pady=(20, 0))

    tk.Label(
        header,
        text="Secure • Reliable • Trusted Banking",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#d7e8ff"
    ).pack()

    # ================= MAIN CARD =================
    card = tk.Frame(
        root,
        bg="white",
        bd=1,
        relief="solid",
        padx=40,
        pady=40
    )
    card.pack(pady=60)

    tk.Label(
        card,
        text="Welcome",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack()

    tk.Label(
        card,
        text="Choose how you want to continue",
        font=("Segoe UI", 11),
        bg="white",
        fg="gray40"
    ).pack(pady=(5, 30))

    # ================= BUTTON STYLE =================
    btn_style = {
        "font": ("Segoe UI", 12, "bold"),
        "bg": "#0f4c81",
        "fg": "white",
        "activebackground": "#1565a9",
        "activeforeground": "white",
        "width": 24,
        "height": 2,
        "bd": 0,
        "cursor": "hand2"
    }

    tk.Button(
        card,
        text="Admin Login",
        command=lambda: adminLogin(root),
        **btn_style
    ).pack(pady=8)

    tk.Button(
        card,
        text="User Login",
        command=lambda: userLogin(root),
        **btn_style
    ).pack(pady=8)

    tk.Button(
        card,
        text="Create New Account",
        command=lambda: createAccountPage(root),
        **btn_style
    ).pack(pady=8)

    # ================= FOOTER =================
    tk.Label(
        root,
        text="© 2026 BMS Banking System",
        bg="#edf2f7",
        fg="gray50",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)

def officerInterfacePage(root):
    clear_root(root)
    officerInterface(root)

def adminLogin(root):
    clear_root(root)

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
        text="Administrator Login",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= LOGIN CARD =================
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
        text="Admin Login",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack(pady=(0, 25))

    # Admin ID
    tk.Label(
        card,
        text="Employee ID",
        bg="white",
        fg="#374151",
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ).pack(fill="x")

    admin_id = tk.Entry(
        card,
        font=("Segoe UI", 11),
        width=32
    )
    admin_id.pack(pady=(5, 18), ipady=5)

    # Password
    tk.Label(
        card,
        text="Password",
        bg="white",
        fg="#374151",
        font=("Segoe UI", 11, "bold"),
        anchor="w"
    ).pack(fill="x")

    admin_password = tk.Entry(
        card,
        show="*",
        font=("Segoe UI", 11),
        width=32
    )
    admin_password.pack(pady=(5, 20), ipady=5)

    # Message Label
    messageLabel = tk.Label(
        card,
        text="",
        bg="white",
        fg="red",
        font=("Segoe UI", 10, "bold")
    )
    messageLabel.pack(pady=(0, 15))

    # Login Button
    tk.Button(
        card,
        text="Login",
        font=("Segoe UI", 11, "bold"),
        bg="#0f4c81",
        fg="white",
        activebackground="#1565a9",
        activeforeground="white",
        bd=0,
        width=22,
        height=2,
        cursor="hand2",
        command=lambda: checkAdminStatus(
            root,
            messageLabel,
            admin_id.get(),
            admin_password.get()
        )
    ).pack(pady=(0, 10))

    # Back Button
    tk.Button(
        card,
        text="← Back",
        font=("Segoe UI", 10),
        bg="#e5e7eb",
        fg="#111827",
        bd=0,
        width=22,
        height=2,
        cursor="hand2",
        command=lambda: landing(root)
    ).pack()

    # Footer
    tk.Label(
        root,
        text="Authorized Personnel Only",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)

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

    # Back Button
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 10),
        bg="#e5e7eb",
        fg="#111827",
        bd=0,
        width=22,
        height=2,
        cursor="hand2",
        command=lambda: landing(root)
    ).pack()
