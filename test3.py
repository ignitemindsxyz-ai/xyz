import mysql.connector

conn   = mysql.connector.connect(host='localhost', user='root', password='',)

cursor = conn.cursor()


# List all databases:

cursor.execute('SHOW DATABASES')

for (db,) in cursor.fetchall(): print(f'  {db}')

cursor.execute('USE school_db')


student_id = input("Enter Student ID: ")

cursor.execute(
    "SELECT * FROM students WHERE id=%s",
    (student_id,)
)

student = cursor.fetchone()

if student:
    print("Current Data:")
    print(student)

    name = input(f"Name [{student[1]}]: ") or student[1]
    email = input(f"Email [{student[2]}]: ") or student[2]
    age = input(f"Age [{student[3]}]: ") or student[3]
    course = input(f"Course [{student[4]}]: ") or student[4]
    grade = input(f"Grade [{student[5]}]: ") or student[5]

    cursor.execute(
        """
        UPDATE students
        SET name=%s,
            email=%s,
            age=%s,
            course=%s,
            grade=%s
        WHERE id=%s
        """,
        (
            name,
            email,
            age,
            course,
            grade,
            student_id
        )
    )

    conn.commit()
    print("Student updated successfully!")

else:
    print("Student not found!")

cursor.execute('SHOW DATABASES')