import tkinter as tk
from userinterface import userInterface
from adminInterface import adminInterface
from createAccount import createAccount


root = tk.Tk()
root.title("BMS Bank")
root.geometry("700x800")
root.resizable(False, False)
root.configure(bg="lightblue")


def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

def landing():
    clear_root()

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
        command=adminLogin
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
        command=userLogin
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
        command=createAccountPage
    )
    createAccount.pack(pady=10)

def adminLogin():
    clear_root()

    tk.Label(
        root,
        text="Welcome to BMS Banking System",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    tk.Label(
        root,
        text="Admin Login",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=30)

    tk.Label(
        root,
        text="phone no: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()

    username = tk.Entry(root, width=30)
    username.pack(pady=5)

    tk.Label(
        root,
        text="Password",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()

    password = tk.Entry(root, show="*", width=30)
    password.pack(pady=5)

    tk.Button(
        root,
        text="Login",
        bg="#0272ea",
        fg="white",
        command=adminPage
    ).pack(pady=20)

    tk.Button(
        root,
        text="Back",
        command=landing
    ).pack()

def userLogin():
    clear_root()
    userPage()
    
def adminPage():
    clear_root()
    adminInterface(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=landing
    ).pack()

def userPage():
    clear_root()
    userInterface(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=landing
    ).pack()

def createAccountPage():
    clear_root()
    createAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=landing
    ).pack()


landing()
root.mainloop()