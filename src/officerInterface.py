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
from activateAdminAccount import activateAdminId



def clear_root(root):
    for widget in root.winfo_children():
        widget.destroy()

def renderLanding(root):
    from landing import landing
    landing(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def blockAdminPage(root):
    clear_root(root)
    blockAdmin(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def activateAdminPage(root):
    clear_root(root)
    activateAdminId(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def deleteAdminPage(root):
    clear_root(root)
    deleteAdmin(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def blockAccountPage(root):
    clear_root(root)
    blockAccount(root)

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
        command=lambda: officerInterface(root)
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
        command=lambda: officerInterface(root)
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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def viewTransactionsPage(root):
    clear_root(root)
    viewTransactions(root, False)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def viewAllTransactionsPage(root):
    clear_root(root)
    viewAllTransactions(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def viewAllAccountPage(root):
    clear_root(root)
    viewAllAccounts(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def createAdminAccountPage(root):
    clear_root(root)
    createAdminAccount(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=5)

def searchAccountPage(root):
    clear_root(root)
    searchAccount(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def searchAdminPage(root):
    clear_root(root)
    searchAdmin(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def viewAllAdminPage(root):
    clear_root(root)
    viewAllAdmin(root)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

def officerInterface(root):
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
        text="Officer Dashboard",
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
        "width": 20,
        "height": 5,
        "bd": 1,
        "relief": "solid",
        "cursor": "hand2"
    }

    # ---------------- Row 1 ----------------

    tk.Button(
        grid,
        text="➕\nCreate Admin",
        command=lambda: createAdminAccountPage(root),
        **btn_style
    ).grid(row=0, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="🗑\nDelete Admin",
        command=lambda: deleteAdminPage(root),
        **btn_style
    ).grid(row=0, column=1, padx=15, pady=15)

    tk.Button(
        grid,
        text="🚫\nBlock Admin",
        command=lambda: blockAdminPage(root),
        **btn_style
    ).grid(row=0, column=2, padx=15, pady=15)

    # ---------------- Row 2 ----------------

    tk.Button(
        grid,
        text="✅\nReactivate Admin",
        command=lambda: activateAdminPage(root),
        **btn_style
    ).grid(row=1, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="🗑\nDelete User",
        command=lambda: deleteAccountPage(root),
        **btn_style
    ).grid(row=1, column=1, padx=15, pady=15)

    tk.Button(
        grid,
        text="🚫\nBlock User",
        command=lambda: blockAccountPage(root),
        **btn_style
    ).grid(row=1, column=2, padx=15, pady=15)

    # ---------------- Row 3 ----------------

    tk.Button(
        grid,
        text="🔍\nSearch User",
        command=lambda: searchAccountPage(root),
        **btn_style
    ).grid(row=2, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="👤\nSearch Admin",
        command=lambda: searchAdminPage(root),
        **btn_style
    ).grid(row=2, column=1, padx=15, pady=15)

    tk.Button(
        grid,
        text="🛡\nView Admins",
        command=lambda: viewAllAdminPage(root),
        **btn_style
    ).grid(row=2, column=2, padx=15, pady=15)

    # ---------------- Row 4 ----------------

    tk.Button(
        grid,
        text="👥\nView Users",
        command=lambda: viewAllAccountPage(root),
        **btn_style
    ).grid(row=3, column=0, padx=15, pady=15)

    tk.Button(
        grid,
        text="📄\nTransactions",
        command=lambda: viewTransactionsPage(root),
        **btn_style
    ).grid(row=3, column=1, padx=15, pady=15)

    tk.Button(
        grid,
        text="📊\nAll Transactions",
        command=lambda: viewAllTransactionsPage(root),
        **btn_style
    ).grid(row=3, column=2, padx=15, pady=15)

    # Equal column sizes
    grid.grid_columnconfigure(0, weight=1)
    grid.grid_columnconfigure(1, weight=1)
    grid.grid_columnconfigure(2, weight=1)

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
        command=lambda: officerInterface(root)
    ).pack(pady=30)

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Officer Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=15)
