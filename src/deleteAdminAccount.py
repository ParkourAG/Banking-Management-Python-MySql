import tkinter as tk
from db_config import db_connect
from db_operations import isAdminExist


def delete_admin_account(messageLabel, admin_id):
    try:
        db= db_connect()

        if isAdminExist(db, admin_id):
            cursor=db.cursor()
            sql= f"UPDATE employees \
                            SET admin_status = 'inactive', \
                                leave_date= (CURRENT_DATE) \
                            WHERE emp_id = '{admin_id}';"
            cursor.execute(sql)
            db.commit()

            # show message
            messageLabel.config(text=f"Admin Id no:{admin_id} is deleted successfully.")

        else:
            messageLabel.config(text=f"Admin Id no:{admin_id} dosent exist.")

    except Exception as e:
        messageLabel.config(text=f"Something went wrong please try again.")
        print(f"Error: {e}")
    finally:
        db.close()

def deleteAdmin(root):
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
        text="Delete Administrator Account",
        font=("Segoe UI", 11),
        bg="#0f4c81",
        fg="#dbeafe"
    ).pack()

    # ================= CARD =================
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
        text="Delete Admin Account",
        font=("Segoe UI", 20, "bold"),
        bg="white",
        fg="#0f4c81"
    ).pack(pady=(0, 25))

    # -------- Admin ID --------
    tk.Label(
        card,
        text="Administrator ID",
        font=("Segoe UI", 11, "bold"),
        bg="white",
        fg="#374151",
        anchor="w"
    ).pack(fill="x")

    entry_id = tk.Entry(
        card,
        width=35,
        font=("Segoe UI", 11)
    )
    entry_id.pack(ipady=5, pady=(5, 20))

    # -------- Message --------
    messageLabel = tk.Label(
        card,
        text="",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red"
    )
    messageLabel.pack(pady=(0, 15))

    # -------- Delete Button --------
    tk.Button(
        card,
        text="Delete Account",
        font=("Segoe UI", 11, "bold"),
        bg="#dc2626",
        fg="white",
        activebackground="#b91c1c",
        activeforeground="white",
        bd=0,
        width=24,
        height=2,
        cursor="hand2",
        command=lambda: delete_admin_account(
            messageLabel,
            entry_id.get()
        )
    ).pack()

    # ================= FOOTER =================
    tk.Label(
        root,
        text="Officer Access • BMS Banking System",
        bg="#edf2f7",
        fg="gray45",
        font=("Segoe UI", 10)
    ).pack(side="bottom", pady=20)
