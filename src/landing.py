import tkinter as tk
from userinterface import userInterface
from adminInterface import adminInterface
from createAccount import createAccount
from db_operations import checkAdminPassword


# root = tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.resizable(False, False)
# root.configure(bg="lightblue")


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

# def checkPassword(, admin_id, password, messageLabel):



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

    tk.Button(
        root,
        text="Login",
        bg="#0272ea",
        fg="white",
        command=lambda:adminPage(root)
    ).pack(pady=20)

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    tk.Button(
        root,
        text="Back",
        command=lambda:adminPage(root)
    ).pack()

    messageLabel.pack(pady=10)

def userLogin(root):
    clear_root(root)
    userPage(root)
    
def adminPage(root):

    # if Wrong password



    # If Login is Successfull
    clear_root(root)
    adminInterface(root)

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