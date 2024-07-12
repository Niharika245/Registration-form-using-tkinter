import tkinter as tk
from tkinter import messagebox
import re

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    phone = entry_phone.get()
    address = entry_address.get("1.0", tk.END).strip()

    # Basic validation checks
    if not name or not email or not age or not password or not confirm_password or not phone or not address:
        messagebox.showwarning("Input Error", "All fields are required")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Input Error", "Invalid email format")
        return
    
    if password != confirm_password:
        messagebox.showwarning("Input Error", "Passwords do not match")
        return
    
    if not age.isdigit() or int(age) <= 0:
        messagebox.showwarning("Input Error", "Invalid age")
        return
    
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showwarning("Input Error", "Invalid phone number. It should be a 10-digit number.")
        return
    
    # For now, just display the entered information
    messagebox.showinfo("Form Submitted", f"Name: {name}\nEmail: {email}\nAge: {age}\nPhone: {phone}\nAddress: {address}")

# Set up the main application window
root = tk.Tk()
root.title("Registration Form")

# Create and place the form fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=3, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=3, column=1, padx=10, pady=5)

label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.grid(row=4, column=0, padx=10, pady=5)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.grid(row=4, column=1, padx=10, pady=5)

label_phone = tk.Label(root, text="Phone Number:")
label_phone.grid(row=5, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=5, column=1, padx=10, pady=5)

label_address = tk.Label(root, text="Address:")
label_address.grid(row=6, column=0, padx=10, pady=5)
entry_address = tk.Text(root, height=4, width=30)
entry_address.grid(row=6, column=1, padx=10, pady=5)

# Create and place the submit button
button_submit = tk.Button(root, text="Submit", command=submit_form)
button_submit.grid(row=7, column=0, columnspan=2, pady=20)

# Start the main event loop
root.mainloop()