
import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = entry_name.get().strip()

    try:
        age_text = entry_age.get().strip()

        if not name:
            messagebox.showerror("Error", "Please enter your name")
            return

        age = int(age_text)

        if age < 0:
            messagebox.showerror("Error", "Age cannot be negative")
        elif age >= 18:
            result_label.config(
                text=f"{name} is eligible to vote."
            )
        else:
            result_label.config(
                text=f"{name} is not eligible to vote."
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age")

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("400x250")

tk.Label(root, text="Enter Your Name").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Enter Your Age").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack()

tk.Button(
    root, text="Check Eligibility", command=check_eligibility
).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
