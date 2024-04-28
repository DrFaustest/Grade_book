import tkinter as tk
from tkinter import messagebox
import student.student_gui
import student.student_db

def validate_student_credentials(student_id, last_name):
    # Checks against the database
    return student.student_db.check_student_credentials(student_id, last_name)

def create_login_window():
    login_window = tk.Toplevel()
    login_window.title("Student Login")

    tk.Label(login_window, text="Student ID:").grid(row=0, column=0)
    id_entry = tk.Entry(login_window)
    id_entry.grid(row=0, column=1)

    tk.Label(login_window, text="Last Name:").grid(row=1, column=0)
    last_name_entry = tk.Entry(login_window)
    last_name_entry.grid(row=1, column=1)

    submit_button = tk.Button(login_window, text="Submit", command=lambda: login(id_entry.get(), last_name_entry.get()))
    submit_button.grid(row=2, column=0, columnspan=2)

def login(student_id, last_name):
    if validate_student_credentials(student_id, last_name):
        student.student_gui.show_student_dashboard(student_id)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

def view_grades(student_id):
    return student.student_db.get_grades_for_student(student_id)
