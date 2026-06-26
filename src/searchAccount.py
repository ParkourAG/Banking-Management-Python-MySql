import tkinter as tk
from tkinter import ttk
import pandas as pd
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

table=None

def search_account(acc_id, name, phone, email):
    try:
        db=db_connect()
        cursor=db.cursor()
        sql=f"SELECT * FROM accounts_details WHERE id='{acc_id}' OR acc_name='{name}' OR ph_no='{phone}' OR email='{email}';"
        cursor.execute(sql)
        results=cursor.fetchall()

        # print(results)
        return results
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()
        
def renderAccountInfo(root, messageLabel, acc_id, name, phone, email):
        data=search_account(acc_id, name, phone, email)

        # clearing previous table
        global table
        if table:
            table.destroy()

        # print(f"Data: {data}")

        # if result is not empty
        if len(data)>0:
            df = pd.DataFrame(data)

            messageLabel.config(text="")

            table = ttk.Treeview(root, columns=list(df.columns), show="headings", height=min(len(df), 10))
            # Create column headings
            for col in df.columns:
                table.heading(col, text=col)
                table.column(col, width=100)
            # Insert rows
            for row in df.itertuples(index=False):
                table.insert("", tk.END, values=row)

            table.pack()
        else:
            messageLabel.config(text="No Account found")

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
        text="Enter Account no: ",
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

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )
    
    # Button Search account
    btn_createAccount= tk.Button(
        root,
        text="Search Account",
        command=lambda:renderAccountInfo(root, messageLabel, entry_id.get(), entry_username.get(), entry_phone.get(), entry_email.get())
    )
    btn_createAccount.pack(pady=20)
    
    messageLabel.pack(pady=10)


# searchAccount(root)
# root.mainloop()