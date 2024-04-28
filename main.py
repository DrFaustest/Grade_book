import tkinter as tk
import admin.admin_logic
import teacher.teacher_logic
import student.student_logic

def main_window():
    root = tk.Tk()
    root.title("School Management System")

    tk.Label(root, text="Welcome to the School Management System", font=('Helvetica', 16)).pack(pady=20)

    tk.Button(root, text="Admin Login", command=admin.admin_logic.create_login_window).pack(pady=10)
    tk.Button(root, text="Teacher Login", command=teacher.teacher_logic.create_login_window).pack(pady=10)
    tk.Button(root, text="Student Login", command=student.student_logic.create_login_window).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()
