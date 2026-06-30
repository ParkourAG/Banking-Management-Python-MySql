import tkinter as tk
from depositeMoney import depositeMoney
from withdrawMoney import withdrawMoney
from deleteAccount import deleteAccount
from showAccountInfo import showAccountInfo
from viewTransactionsUser import viewTransactions


def renderLanding(root):
    from landing import landing
    landing(root)

def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

def depositeMoneyPage(root):
    clear_root(root)
    depositeMoney(root)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: userInterface(root)
    ).pack(pady=30)

def withdrawMoneyPage(root):
    clear_root(root)
    withdrawMoney(root)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: userInterface(root)
    ).pack(pady=30)

def deleteAccountPage(root):
    clear_root(root)
    deleteAccount(root)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: userInterface(root)
    ).pack(pady=30)

def accountInfoPage(root):
    clear_root(root)
    showAccountInfo(root)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: userInterface(root)
    ).pack(pady=30)

def viewTransactionsPage(root):
    clear_root(root)
    viewTransactions(root, True)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: userInterface(root)
    ).pack(pady=30)

def userInterface(root):
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
        text="Customer Dashboard",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= TITLE =================
    tk.Label(
        root,
        text="Choose an Action",
        font=("Segoe UI", 20, "bold"),
        bg="#edf2f7",
        fg="#0f4c81"
    ).pack(pady=(30, 20))

    # ================= GRID =================
    grid = tk.Frame(root, bg="#edf2f7")
    grid.pack()

    btn_style = {
        "font": ("Segoe UI", 11, "bold"),
        "bg": "#ffffff",
        "fg": "#0f4c81",
        "activebackground": "#e8f1ff",
        "activeforeground": "#0f4c81",
        "width": 22,
        "height": 5,
        "bd": 1,
        "relief": "solid",
        "cursor": "hand2"
    }

    # -------- Row 1 --------
    tk.Button(
        grid,
        text="💰\nDeposit Money",
        command=lambda: depositeMoneyPage(root),
        **btn_style
    ).grid(row=0, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="💸\nWithdraw Money",
        command=lambda: withdrawMoneyPage(root),
        **btn_style
    ).grid(row=0, column=1, padx=15, pady=15)

    # -------- Row 2 --------
    tk.Button(
        grid,
        text="👤\nAccount Details",
        command=lambda: accountInfoPage(root),
        **btn_style
    ).grid(row=1, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="📄\nTransactions",
        command=lambda: viewTransactionsPage(root),
        **btn_style
    ).grid(row=1, column=1, padx=15, pady=15)

    # ================= BACK BUTTON =================
    tk.Button(
        root,
        text="← Back",
        font=("Segoe UI", 11, "bold"),
        bg="#6b7280",
        fg="white",
        activebackground="#4b5563",
        activeforeground="white",
        bd=0,
        width=25,
        height=2,
        cursor="hand2",
        command=lambda: renderLanding(root)
    ).pack(pady=30)

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Customer Portal • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
