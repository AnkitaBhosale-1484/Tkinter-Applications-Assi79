
import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "1234":
        result_label.config(text="Login Successful")
        messagebox.showinfo("Login", "Login Successful")
    else:
        result_label.config(text="Invalid Username or Password")
        messagebox.showerror(
            "Login Failed", "Invalid Username or Password"
        )

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("350x250")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
