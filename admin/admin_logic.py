import tkinter as tk
from tkinter import messagebox
import admin.admin_gui

def validate_credentials(username, password):
    # Placeholder for credential validation logic
    if username == "admin" and password == "admin":
        return True
    return False

def create_login_window():
    login_window = tk.Toplevel()
    login_window.title("Admin Login")

    tk.Label(login_window, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.grid(row=1, column=1)

    submit_button = tk.Button(login_window, text="Submit", command=lambda: login(username_entry.get(), password_entry.get()))
    submit_button.grid(row=2, column=0, columnspan=2)

def login(username, password):
    if validate_credentials(username, password):
        admin.admin_gui.show_admin_dashboard()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")
