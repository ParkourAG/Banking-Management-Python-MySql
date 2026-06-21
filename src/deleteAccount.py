import tkinter as tk
from db_config import db_connect

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def delete_account(acc_id):
    # acc_id=input("Enter Account id to delete from bank database: ")
    try:
        db= db_connect()
        cursor=db.cursor()

        sql= f"DELETE FROM accounts_details WHERE id='{acc_id}';"
        cursor.execute(sql)
        db.commit()

        print("your Account is deleted successfully..")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def deleteAccount(root):

    # heading
    tk.Label(
        root,
        text="Delete Account",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter Account Id
    tk.Label(
        root,
        text="Enter Account Number: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack(pady=(40, 0))
    entry_id=tk.Entry(root, width=30)
    entry_id.pack(pady=(5,20))

    # Enter Phone number
    tk.Label(
        root,
        text="Enter Phone no: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()
    tk.Entry(root, width=30).pack(pady=(5,20))

    # Enter Password
    tk.Label(
        root,
        text="Password",
        bg="lightblue",
        font=("Arial", 12)
    ).pack()
    tk.Entry(root, show="*", width=30).pack(pady=(5,20))

    # Button: Delete Account
    tk.Button(
        root,
        text="Delete Account",
        command= lambda:delete_account(entry_id.get())
    ).pack(pady=10)



# deleteAccount(root)
# root.mainloop()