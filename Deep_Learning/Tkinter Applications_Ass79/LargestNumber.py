
import tkinter as tk
from tkinter import messagebox

def find_maximum():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        n3 = float(entry3.get())

        largest = max(n1, n2, n3)
        result_label.config(text=f"Largest Number = {largest:g}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("350x300")

tk.Label(root, text="Enter First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Enter Third Number").pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(
    root, text="Find Maximum", command=find_maximum
).pack(pady=10)

result_label = tk.Label(root, text="Largest Number = ")
result_label.pack()

root.mainloop()
