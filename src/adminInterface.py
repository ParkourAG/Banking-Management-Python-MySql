import tkinter as tk
import sys
from depositeMoney import depositeMoney
from withdrawMoney import withdrawMoney
from deleteAccount import deleteAccount
from viewAllAccounts import viewAllAccounts
from searchUserAccount import searchAccount
from viewTransactions import viewTransactions
from blockAccount import blockAccount
from createAdminAccount import createAdminAccount
from blockAdminAccount import blockAdmin
from deleteAdminAccount import deleteAdmin
from searchAdmin import searchAdmin
from viewAllAdminAccount import viewAllAdmin
from viewAlltransactions import viewAllTransactions


# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

def renderLanding(root):
    from landing import landing
    landing(root)

def depositeMoneyPage(root):
    clear_root(root)
    depositeMoney(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def blockAdminPage(root):
    clear_root(root)
    blockAdmin(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def deleteAdminPage(root):
    clear_root(root)
    deleteAdmin(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def blockAccountPage(root):
    clear_root(root)
    blockAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def withdrawMoneyPage(root):
    clear_root(root)
    withdrawMoney(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def deleteAccountPage(root):
    clear_root(root)
    deleteAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack()

def viewTransactionsPage(root):
    clear_root(root)
    viewTransactions(root, False)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def viewAllTransactionsPage(root):
    clear_root(root)
    viewAllTransactions(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def viewAllAccountPage(root):
    clear_root(root)
    viewAllAccounts(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def createAdminAccountPage(root):
    clear_root(root)
    createAdminAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def searchAccountPage(root):
    clear_root(root)
    searchAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def searchAdminPage(root):
    clear_root(root)
    searchAdmin(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def viewAllAdminPage(root):
    clear_root(root)
    viewAllAdmin(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:adminInterface(root)
    ).pack(pady=10)

def adminInterface(root):
    clear_root(root)

    # label: Choose your action:
    heading= tk.Label(
        root,
        text="Choose your action:",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    )
    heading.pack(pady=20)

    # create Admin account
    deleteAccount= tk.Button(
        root,
        text="Create Admin Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:createAdminAccountPage(root)
    )
    deleteAccount.pack(pady=10)

    # Delete Admin account
    deleteAccount= tk.Button(
        root,
        text="Delete Admin Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:deleteAdminPage(root)
    )
    deleteAccount.pack(pady=10)
    
    # Block Admin account
    deleteAccount= tk.Button(
        root,
        text="Block Admin Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:blockAdminPage(root)
    )
    deleteAccount.pack(pady=10)

    # delete User account
    deleteAccount= tk.Button(
        root,
        text="Delete User Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:deleteAccountPage(root)
    )
    deleteAccount.pack(pady=10)

    # Block user Account
    searchAccount= tk.Button(
        root,
        text="Block user Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:blockAccountPage(root)
    )
    searchAccount.pack(pady=10)

    # Search User Account
    searchAccount= tk.Button(
        root,
        text="Search User Account",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:searchAccountPage(root)
    )
    searchAccount.pack(pady=10)

    # Search Admin
    searchAccount= tk.Button(
        root,
        text="Search Admin",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:searchAdminPage(root)
    )
    searchAccount.pack(pady=10)

    # view all User accounts
    transactions= tk.Button(
        root,
        text="View all User accounts",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:viewAllAdminPage(root)
    )
    transactions.pack(pady=10)
    
    # view all Admin
    transactions= tk.Button(
        root,
        text="View all Admin",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:viewAllAccountPage(root)
    )
    transactions.pack(pady=10)
    

    # search transactions
    transactions= tk.Button(
        root,
        text="Search Transactions",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:viewTransactionsPage(root)
    )
    transactions.pack(pady=10)

    # view all transactions
    transactions= tk.Button(
        root,
        text="View All transactions",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:viewAllTransactionsPage(root)
    )
    transactions.pack(pady=10)

    # Back to Login Button
    tk.Button(
        root,
        text="Back to Login",
        padx=10,
        pady=5,
        command=lambda:renderLanding(root)
    ).pack()


# adminInterface(root)
# root.mainloop()