import tkinter as tk
from tkinter import messagebox

def validate_login(user_type, username='', password='', id='', last_name=''):
    if user_type == 'admin':
        if username == 'admin' and password == 'admin':
            messagebox.showinfo("Login Success", "Admin login successful!")
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password.")
    elif user_type in ['teacher', 'student']:
        # Placeholder validation logic
        if id.isdigit() and last_name:  # Simplistic check; replace with database check later
            messagebox.showinfo("Login Success", f"{user_type.capitalize()} login successful!")
        else:
            messagebox.showerror("Login Failed", "Invalid ID or Last Name.")
    else:
        messagebox.showerror("Login Failed", "Invalid user type.")

def create_login_window(user_type):
    login_window = tk.Toplevel()
    login_window.title(f"{user_type.capitalize()} Login")

    tk.Label(login_window, text=f"{user_type.capitalize()} Username:").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    tk.Label(login_window, text=f"{user_type.capitalize()} Password:").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.grid(row=1, column=1)

    submit_button = tk.Button(login_window, text="Submit", command=lambda: validate_login(user_type, username=username_entry.get(), password=password_entry.get()))
    submit_button.grid(row=2, column=0, columnspan=2)

def main_window():
    root = tk.Tk()
    root.title("School Management System")

    tk.Label(root, text="Welcome to the School Management System", font=('Helvetica', 16)).pack(pady=20)

    tk.Button(root, text="Admin Login", command=lambda: create_login_window('admin')).pack(pady=10)
    tk.Button(root, text="Teacher Login", command=lambda: create_login_window('teacher')).pack(pady=10)
    tk.Button(root, text="Student Login", command=lambda: create_login_window('student')).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
