import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def insert_data(conn, table, data):
    """
    Insert mock data into the table
    """
    cur = conn.cursor()
    columns = ', '.join(data.keys())
    placeholders = ':'+', :'.join(data.keys())
    sql = 'INSERT INTO {} ({}) VALUES ({})'.format(table, columns, placeholders)
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def main():
    database = "school_grades.db"
    
    # Create a database connection
    conn = create_connection(database)

    # Define mock data for all tables including ClassTeachers and ClassStudents
    subjects = [{'subject_code': 'SCI', 'subject_name': 'Science'}, {'subject_code': 'MATH', 'subject_name': 'Mathematics'}]
    teachers = [{'teacher_id': 1, 'first_name': 'John', 'last_name': 'Doe', 'field_of_study': 'SCI'}, {'teacher_id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'field_of_study': 'MATH'}]
    students = [{'student_id': 1, 'first_name': 'Alice', 'last_name': 'Brown'}, {'student_id': 2, 'first_name': 'Bob', 'last_name': 'Davis'}]
    classes = [{'class_id': 1, 'subject_code': 'SCI', 'year_semester': 202301, 'instance': 1}, {'class_id': 2, 'subject_code': 'MATH', 'year_semester': 202301, 'instance': 1}]
    assignments = [{'assignment_id': 1, 'class_id': 1, 'title': 'Lab Report', 'description': 'Report on chemistry lab work.'}, {'assignment_id': 2, 'class_id': 2, 'title': 'Math Quiz', 'description': 'Quiz covering algebra topics.'}]
    grades = [{'grade_id': 1, 'assignment_id': 1, 'student_id': 1, 'grade': 85}, {'grade_id': 2, 'assignment_id': 2, 'student_id': 2, 'grade': 90}]
    class_teachers = [{'class_id': 1, 'teacher_id': 1}, {'class_id': 2, 'teacher_id': 2}]
    class_students = [{'class_id': 1, 'student_id': 1}, {'class_id': 2, 'student_id': 2}]

    with conn:
        # Insert mock data into each table
        for subject in subjects:
            insert_data(conn, 'Subjects', subject)
        for teacher in teachers:
            insert_data(conn, 'Teachers', teacher)
        for student in students:
            insert_data(conn, 'Students', student)
        for cls in classes:
            insert_data(conn, 'Classes', cls)
        for assignment in assignments:
            insert_data(conn, 'Assignments', assignment)
        for grade in grades:
            insert_data(conn, 'Grades', grade)
        for ct in class_teachers:
            insert_data(conn, 'ClassTeachers', ct)
        for cs in class_students:
            insert_data(conn, 'ClassStudents', cs)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
