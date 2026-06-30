import tkinter as tk
from landing import landing
from db_config import db_connect

db=db_connect

root = tk.Tk()
root.title("BMS Bank")
root.geometry("700x800")
root.resizable(True, True)
root.configure(bg="#ffffff")


landing(root)

root.mainloop()