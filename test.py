import pandas as pd
import tkinter as tk
from tkinter import ttk

file_path = '/Users/danny/Documents/TVDI_Project_LTC/CSV檔案/台北市長照機構床位數整理表.csv'
df = pd.read_csv(file_path)


root = tk.Tk()
root.title("台北市長照機構床位數整理表")
root.geometry("800x800")


tree = ttk.Treeview(root)
tree["columns"] = df.columns.tolist()
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)


for index, row in df.iterrows():
    tree.insert("", "end", values=row.tolist())

tree.pack(expand=True, fill="both")

root.mainloop()