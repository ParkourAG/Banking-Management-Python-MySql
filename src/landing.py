import tkinter as tk
from userinterface import userInterface
from adminInterface import adminInterface
from createAccount import createAccount


# root = tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.resizable(False, False)
# root.configure(bg="lightblue")


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

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

def adminLogin(root):
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
        command=lambda:adminPage(root)
    ).pack(pady=20)

    tk.Button(
        root,
        text="Back",
        command=lambda:landing(root)
    ).pack()

def userLogin(root):
    clear_root(root)
    userPage(root)
    
def adminPage(root):
    clear_root(root)
    adminInterface(root)

    # tk.Button(
    #     root,
    #     text="Back",
    #     padx=10,
    #     pady=5,
    #     command=lambda:landing(root)
    # ).pack()

def userPage(root):
    clear_root(root)
    userInterface(root)

    # tk.Button(
    #     root,
    #     text="Back",
    #     padx=10,
    #     pady=5,
    #     command=lambda:landing(root)
    # ).pack()

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