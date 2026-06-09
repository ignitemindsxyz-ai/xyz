import mysql.connector

conn   = mysql.connector.connect(host='localhost', user='root', password='',)

cursor = conn.cursor()

cursor.execute('USE school_db')

while True:
    print("===== School Database =====")
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. View students")
    print("5. Add courses")
    print("6. Add in enrollments")
    print("7. Exit")
    action = input("What would you like to do?(Default : 1): ").strip()

    if action == "1" or action == "":
        student_name = input("Name? : ").title()
        student_email = input("E-mail adderss? : ")
        student_age = input("Age? : ")
        student_grade = input("Grade? : ")

        sql = "INSERT INTO students(name, email, age, grade) VALUES (%s, %s, %s, %s)"
        values = (student_name, student_email, student_age, student_grade)

        cursor.execute(sql, values)
        conn.commit()


    elif action == "2":
        del_student = input("Which student would you like to delete?(id): ")
        
        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (del_student,))
        conn.commit()

    elif action == "3":
        student_id = input("Enter Student ID: ")
        cursor.execute(
            "SELECT * FROM students WHERE id=%s",
            (student_id,)
        )
        student = cursor.fetchone()
        if student:
            print("Current name", student[1])
            print("Current E-mail", student[2])
            print("Current age", student[3])
            print("Current course", student[4])
            print("Current grade", student[5])
            new_name = input("New name: ")
            new_email = input("New E-mail: ")
            new_age = input("New age: ")
            new_course = input("New course: ")
            new_grade = input("New grade: ")
            cursor.execute(
                "UPDATE students SET name=%s, email=%s, age=%s, course=%s, grade=%s WHERE id=%s",
                (new_name, new_email, new_age, new_course, new_grade, student_id)
            )
            conn.commit()
        else:
            print("Student not found.")

    elif action == "4":
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        print("| ID | Name                  | E-mail           | Age | Course   | Grade |")
        print("=" *75)
        for row in cursor.fetchall():
            print(
                f"| {row[0]:<2} | {row[1]:<21} | {row[2]:<16} |"
                f" {row[3]:<3} | {row[4]:<8} | {row[5]:<5} |"
            )

    elif action == "5":
        student_course = input("Course? : ")
        student_credits = input("Total Credits : ")
        student_instructor = input("Instructor? : ").title()

        sql = "INSERT INTO courses (course, credits, instructor) VALUES (%s, %s, %s)"
        values = (student_course, student_credits, student_instructor)

        cursor.execute(sql, values)
        conn.commit()

    elif action == "6":
        view = input("Which student would you like to enroll?(ID) : ")
        select_course = input("And in which course?(1 for Science, 2 for Management) : ").strip().lower()
        sql = "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)"
        values = (view, select_course)

        cursor.execute(sql, values)
        conn.commit()

    elif action == "7":
        print("Exiting.....")
        break

    else:
        print("Invalid option.")


cursor.close()
conn.close()