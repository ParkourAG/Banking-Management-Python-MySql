# import tkinter as tk
# import pandas as pd

# data = [
#     [1, "Alice", 85],
#     [2, "Bob", 90],
#     [3, "Charlie", 78]
# ]

# df = pd.DataFrame(data, columns=["ID", "Name", "Marks"])

# root = tk.Tk()
# root.title("DataFrame Viewer")

# text = tk.Text(root, width=40, height=10)
# text.pack()

# text.insert(tk.END, df.to_string(index=False))

# root.mainloop()


import tkinter as tk
from tkinter import ttk
import pandas as pd

data = [
    [1, "Alice", 85],
    [2, "Bob", 90],
    [3, "Charlie", 78]
]

df = pd.DataFrame(data, columns=["ID", "Name", "Marks"])

root = tk.Tk()
root.title("DataFrame Table")

tree = ttk.Treeview(root, columns=list(df.columns), show="headings")

# Create column headings
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

# Insert rows
for row in df.itertuples(index=False):
    tree.insert("", tk.END, values=row)

tree.pack(fill="both", expand=True)

root.mainloop()