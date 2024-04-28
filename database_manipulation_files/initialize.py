import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    database = "school_grades.db"

    sql_create_subjects_table = """ CREATE TABLE IF NOT EXISTS Subjects (
                                        subject_code VARCHAR PRIMARY KEY,
                                        subject_name VARCHAR NOT NULL
                                    ); """

    sql_create_classes_table = """CREATE TABLE IF NOT EXISTS Classes (
                                    class_id INTEGER PRIMARY KEY,
                                    subject_code VARCHAR NOT NULL,
                                    year_semester INT NOT NULL,
                                    instance INT NOT NULL,
                                    FOREIGN KEY (subject_code) REFERENCES Subjects (subject_code)
                                );"""

    sql_create_teachers_table = """CREATE TABLE IF NOT EXISTS Teachers (
                                    teacher_id INTEGER PRIMARY KEY,
                                    first_name VARCHAR NOT NULL,
                                    last_name VARCHAR NOT NULL,
                                    field_of_study VARCHAR NOT NULL,
                                    FOREIGN KEY (field_of_study) REFERENCES Subjects (subject_code)
                                );"""

    sql_create_students_table = """CREATE TABLE IF NOT EXISTS Students (
                                    student_id INTEGER PRIMARY KEY,
                                    first_name VARCHAR NOT NULL,
                                    last_name VARCHAR NOT NULL
                                );"""

    sql_create_assignments_table = """CREATE TABLE IF NOT EXISTS Assignments (
                                        assignment_id INTEGER PRIMARY KEY,
                                        class_id INT NOT NULL,
                                        title VARCHAR NOT NULL,
                                        description TEXT,
                                        FOREIGN KEY (class_id) REFERENCES Classes (class_id)
                                    );"""

    sql_create_grades_table = """CREATE TABLE IF NOT EXISTS Grades (
                                    grade_id INTEGER PRIMARY KEY,
                                    assignment_id INT NOT NULL,
                                    student_id INT NOT NULL,
                                    grade INT NOT NULL,
                                    FOREIGN KEY (assignment_id) REFERENCES Assignments (assignment_id),
                                    FOREIGN KEY (student_id) REFERENCES Students (student_id)
                                );"""

    sql_create_class_teachers_table = """CREATE TABLE IF NOT EXISTS ClassTeachers (
                                            class_id INT NOT NULL,
                                            teacher_id INT NOT NULL,
                                            PRIMARY KEY (class_id, teacher_id),
                                            FOREIGN KEY (class_id) REFERENCES Classes (class_id),
                                            FOREIGN KEY (teacher_id) REFERENCES Teachers (teacher_id)
                                        );"""

    sql_create_class_students_table = """CREATE TABLE IF NOT EXISTS ClassStudents (
                                            class_id INT NOT NULL,
                                            student_id INT NOT NULL,
                                            PRIMARY KEY (class_id, student_id),
                                            FOREIGN KEY (class_id) REFERENCES Classes (class_id),
                                            FOREIGN KEY (student_id) REFERENCES Students (student_id)
                                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_subjects_table)
        create_table(conn, sql_create_classes_table)
        create_table(conn, sql_create_teachers_table)
        create_table(conn, sql_create_students_table)
        create_table(conn, sql_create_assignments_table)
        create_table(conn, sql_create_grades_table)
        create_table(conn, sql_create_class_teachers_table)
        create_table(conn, sql_create_class_students_table)
    else:
        print("Error! Cannot create the database connection.")

    # close the connection
    conn.close()

if __name__ == '__main__':
    main()
