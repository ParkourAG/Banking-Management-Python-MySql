import tkinter as tk
from depositeMoney import depositeMoney
from withdrawMoney import withdrawMoney
from deleteAccount import deleteAccount
from showAccountInfo import showAccountInfo
from viewTransactions import viewTransactions
# root= tk.Tk()

def renderLanding(root):
    from landing import landing
    landing(root)


def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

def depositeMoneyPage(root):
    clear_root(root)
    depositeMoney(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:userInterface(root)
    ).pack()

def withdrawMoneyPage(root):
    clear_root(root)
    withdrawMoney(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:userInterface(root)
    ).pack()

def deleteAccountPage(root):
    clear_root(root)
    deleteAccount(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:userInterface(root)
    ).pack()

def accountInfoPage(root):
    clear_root(root)
    showAccountInfo(root)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:userInterface(root)
    ).pack(pady=10)

def viewTransactionsPage(root):
    clear_root(root)
    viewTransactions(root, True)

    tk.Button(
        root,
        text="Back",
        padx=10,
        pady=5,
        command=lambda:userInterface(root)
    ).pack(pady=10)

def userInterface(root):
    clear_root(root)

    # label: Choose your action:
    heading= tk.Label(
        root,
        text="Choose your action:",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="white"
    )
    heading.pack(pady=30)

    # deposite cash
    creditCash= tk.Button(
        root,
        text="Credit Money",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:depositeMoneyPage(root)
    )
    creditCash.pack(pady=10)

    # withdraw cash
    debitCash= tk.Button(
        root,
        text="Debit Money",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:withdrawMoneyPage(root)
    )
    debitCash.pack(pady=10)

    # # delete account
    # deleteAccount= tk.Button(
    #     root,
    #     text="Delete Account",
    #     font=("Arial", 14, "bold"),
    #     bg="#0272ea",
    #     fg="white",
    #     padx=20,
    #     pady=10,
    #     bd=0,
    #     cursor="hand2",
    #     command=lambda:deleteAccountPage(root)
    # )
    # deleteAccount.pack(pady=10)

    # view account info and balance
    accountInfo= tk.Button(
        root,
        text="View Account Info",
        font=("Arial", 14, "bold"),
        bg="#0272ea",
        fg="white",
        padx=20,
        pady=10,
        bd=0,
        cursor="hand2",
        command=lambda:accountInfoPage(root)
    )
    accountInfo.pack(pady=10)


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


# userInterface(root)
# root.mainloop()