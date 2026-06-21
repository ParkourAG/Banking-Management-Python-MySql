import tkinter as tk
import sys
from depositeMoney import depositeMoney
from withdrawMoney import withdrawMoney
from deleteAccount import deleteAccount
from viewAllAccounts import viewAllAccounts
from searchAccount import searchAccount
from viewTransactions import viewTransactions


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

    # # deposite cash
    # creditCash= tk.Button(
    #     root,
    #     text="Credit Cash",
    #     font=("Arial", 14, "bold"),
    #     bg="#0272ea",
    #     fg="white",
    #     padx=20,
    #     pady=10,
    #     bd=0,
    #     cursor="hand2",
    #     command=lambda:depositeMoneyPage(root)
    # )
    # creditCash.pack(pady=10)

    # # withdraw cash
    # debitCash= tk.Button(
    #     root,
    #     text="Debit Cash",
    #     font=("Arial", 14, "bold"),
    #     bg="#0272ea",
    #     fg="white",
    #     padx=20,
    #     pady=10,
    #     bd=0,
    #     cursor="hand2",
    #     command=lambda:withdrawMoneyPage(root)
    # )
    # debitCash.pack(pady=10)

    # delete account
    deleteAccount= tk.Button(
        root,
        text="Delete Account",
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

    # Search Account
    searchAccount= tk.Button(
        root,
        text="Search Account",
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

    # view all accounts
    transactions= tk.Button(
        root,
        text="View all accounts",
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
    

    # view all transactions
    transactions= tk.Button(
        root,
        text="View last transactions",
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