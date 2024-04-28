import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def display_teacher_view(conn, teacher_id):
    """
    Display classes, assignments, and grades from the perspective of a teacher.
    """
    cur = conn.cursor()

    # Select all classes taught by the teacher
    cur.execute("""
    SELECT class_id, subject_name, year_semester 
    FROM Classes 
    JOIN Subjects ON Classes.subject_code = Subjects.subject_code
    WHERE class_id IN (SELECT class_id FROM ClassTeachers WHERE teacher_id = ?)
    """, (teacher_id,))

    classes = cur.fetchall()
    print(f"\nClasses taught by Teacher ID {teacher_id}:")
    for cls in classes:
        print(f"Class ID: {cls[0]}, Subject: {cls[1]}, Year/Semester: {cls[2]}")

        # Select all assignments for each class
        cur.execute("""
        SELECT assignment_id, title 
        FROM Assignments 
        WHERE class_id = ?
        """, (cls[0],))

        assignments = cur.fetchall()
        print(" Assignments:")
        for assignment in assignments:
            print(f"  Assignment ID: {assignment[0]}, Title: {assignment[1]}")

            # Select all grades for each assignment
            cur.execute("""
            SELECT student_id, grade 
            FROM Grades 
            WHERE assignment_id = ?
            """, (assignment[0],))

            grades = cur.fetchall()
            print("  Grades:")
            for grade in grades:
                print(f"   Student ID: {grade[0]}, Grade: {grade[1]}")

def display_student_view(conn, student_id):
    """
    Display classes and grades from the perspective of a student.
    """
    cur = conn.cursor()

    # Select all classes the student is enrolled in
    cur.execute("""
    SELECT Classes.class_id, subject_name, year_semester 
    FROM ClassStudents 
    JOIN Classes ON ClassStudents.class_id = Classes.class_id
    JOIN Subjects ON Classes.subject_code = Subjects.subject_code
    WHERE ClassStudents.student_id = ?
    """, (student_id,))

    classes = cur.fetchall()
    print(f"\nClasses for Student ID {student_id}:")
    for cls in classes:
        print(f"Class ID: {cls[0]}, Subject: {cls[1]}, Year/Semester: {cls[2]}")

        # Select all grades for the student in each class
        cur.execute("""
        SELECT Assignments.assignment_id, Assignments.title, Grades.grade 
        FROM Grades 
        JOIN Assignments ON Grades.assignment_id = Assignments.assignment_id
        WHERE Grades.student_id = ? AND Assignments.class_id = ?
        """, (student_id, cls[0]))

        grades = cur.fetchall()
        print(" Grades:")
        for grade in grades:
            print(f"  Assignment ID: {grade[0]}, Title: {grade[1]}, Grade: {grade[2]}")


def fetch_all_data(conn, table_name):
    """ Fetch and print all data from a specified table """
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()

    print(f"Data from {table_name}:")
    for row in rows:
        print(row)

def main():
    database = "school_grades.db"

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        # List of all table names to iterate over
        tables = ['Subjects', 'Classes', 'Teachers', 'Students', 'Assignments', 'Grades', 'ClassTeachers', 'ClassStudents']

        for table in tables:
            fetch_all_data(conn, table)

    else:
        print("Error! Cannot create the database connection.")

    # Display the teacher view for a given teacher_id (e.g., teacher_id = 1)
    display_teacher_view(conn, 1)

    # Display the student view for a given student_id (e.g., student_id = 1)
    display_student_view(conn, 1)

    conn.close()

if __name__ == '__main__':
    main()
