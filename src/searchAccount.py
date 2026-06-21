import tkinter as tk
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def search_account(acc_id, name, phone, email):
    try:
        db=db_connect()
        cursor=db.cursor()
        sql=f"SELECT * FROM accounts_details WHERE id='{acc_id}' OR acc_name='{name}' OR ph_no='{phone}' OR email='{email}';"
        cursor.execute(sql)
        results=cursor.fetchall()

        print(results)
        return results
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
        
def searchAccount(root):

    # heading
    tk.Label(
        root,
        text="Search Account",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter Name
    label_username= tk.Label(
        root,
        text="Enter Name: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_username.pack(pady=(40, 0))

    entry_username = tk.Entry(root, width=30)
    entry_username.pack(pady=(5,30))

    # Enter Phone no
    label_phone= tk.Label(
        root,
        text="Enter phone no: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_phone.pack()

    entry_phone = tk.Entry(root, width=30)
    entry_phone.pack(pady=(5,30))

    # Enter Bank ID
    label_id= tk.Label(
        root,
        text="Enter Bank ID: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_id.pack()

    entry_id = tk.Entry(root, width=30)
    entry_id.pack(pady=(5,30))

    # Enter Email
    label_email= tk.Label(
        root,
        text="Enter Email: ",
        bg="lightblue",
        font=("Arial", 12)
    )
    label_email.pack()

    entry_email = tk.Entry(root, width=30)
    entry_email.pack(pady=(5,30))

    # Button Search account
    btn_createAccount= tk.Button(
        root,
        text="Search Account",
        command=lambda:search_account(entry_id.get(), entry_username.get(), entry_phone.get(), entry_email.get())
    )
    btn_createAccount.pack(pady=20)


# searchAccount(root)
# root.mainloop()