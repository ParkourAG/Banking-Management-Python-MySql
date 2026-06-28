import tkinter as tk
from db_config import db_connect
from db_operations import isAdminExist, isAdminBlocked, isAdminInactive

# root= tk.Tk()
# root.title("BMS Bank")
# root.geometry("700x800")
# root.configure(bg="lightblue")
# root.resizable(False,False)

def activateAdminAccount(messageLabel, admin_id, root):
    try:
        db= db_connect()

#  Check if account exists
        if isAdminExist(db, admin_id):

            # check if account is already blocked
            if isAdminBlocked(db, admin_id) or isAdminInactive(db, admin_id):
                cursor=db.cursor()
                sql= f"UPDATE employees \
                        SET admin_status = 'active' \
                        WHERE emp_id = '{admin_id}';"
                cursor.execute(sql)
                db.commit()

                # printing message
                messageLabel.config(text=f"Admin Id no:{admin_id} is Re-activated successfully.")
            else:
                # printing message
                messageLabel.config(text=f"Admin Id no:{admin_id} is already active.")
        
        else:
            messageLabel.config(text=f"Admin Id no:{admin_id} dosent exist. please type account number correctly.")
            

    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

def activateAdminId(root):

    # heading
    tk.Label(
        root,
        text="Re-activate Admin Account",
        font=("Arial", 30, "bold"),
        bg="lightblue",
        fg="white"
    ).pack(pady=40)

    # Enter Account Id
    tk.Label(
        root,
        text="Enter Admin Id: ",
        bg="lightblue",
        font=("Arial", 12)
    ).pack(pady=(40, 0))
    entry_id=tk.Entry(root, width=30)
    entry_id.pack(pady=(5,20))

    # creating message
    messageLabel=tk.Label(
                    root,
                    font=("Arial", 15, "bold"),
                    bg="lightblue",
                    fg="black"
                )

    # Button: Block Account
    tk.Button(
        root,
        text="Activate Account",
        command= lambda:activateAdminAccount(messageLabel ,entry_id.get(), root)
    ).pack(pady=10)

    # Message
    messageLabel.pack(pady=10)

# activateAdminId(root)
# root.mainloop()
