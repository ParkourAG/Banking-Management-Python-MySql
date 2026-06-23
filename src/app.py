import tkinter as tk
from landing import landing

root = tk.Tk()
root.title("BMS Bank")
root.geometry("700x800")
root.resizable(False, False)
root.configure(bg="lightblue")


landing(root)


root.mainloop()

# create admin login 