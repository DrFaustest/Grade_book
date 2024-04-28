import tkinter as tk
from tkinter import messagebox
import teacher.teacher_gui
import teacher.teacher_db

def validate_teacher_credentials(teacher_id, last_name):
    # This would check the credentials against the database
    return teacher.teacher_db.check_teacher_credentials(teacher_id, last_name)

def create_login_window():
    login_window = tk.Toplevel()
    login_window.title("Teacher Login")

    tk.Label(login_window, text="Teacher ID:").grid(row=0, column=0)
    id_entry = tk.Entry(login_window)
    id_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Last Name:").grid(row=1, column=0)
    last_name_entry = tk.Entry(login_window)
    last_name_entry.grid(row=1, column=1)

    submit_button = tk.Button(login_window, text="Submit", command=lambda: login(id_entry.get(), last_name_entry.get()))
    submit_button.grid(row=2, column=0, columnspan=2)

def login(teacher_id, last_name):
    if validate_teacher_credentials(teacher_id, last_name):
        teacher.teacher_gui.show_teacher_dashboard(teacher_id)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

def add_assignment(class_id, title, description):
    if not title.strip():
        messagebox.showerror("Error", "Title cannot be empty.")
        return False
    return teacher.teacher_db.add_assignment_to_class(class_id, title, description)

def fetch_classes(teacher_id):
    return teacher.teacher_db.get_classes_taught_by(teacher_id)
