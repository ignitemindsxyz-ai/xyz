import mysql.connector

 

conn   = mysql.connector.connect(host='localhost', user='root', password='',)

cursor = conn.cursor()


# List all databases:

cursor.execute('SHOW DATABASES')

for (db,) in cursor.fetchall(): print(f'  {db}')

cursor.execute('USE school_db')

# Inspect table structure:

cursor.execute('DESCRIBE students')

for col in cursor.fetchall():

    print(f'  {col[0]:20} {col[1]:20} Null:{col[2]}')

while True:
    print("===== Stusent Database =====")
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. Exit")
    action = int(input("What would you like to do?(1, 2, 3, 4): "))

    if action == 1:
        student_name = input("Name? : ")
        student_email = input("E-mail adderss? : ")
        student_age = input("Age? : ")
        student_course = input("Course? : ")
        student_grade = input("Grade? : ")

        sql = "INSERT INTO students(name, email, age, course, grade) VALUES (%s, %s, %s, %s, %s)"
        values = (student_name, student_email, student_age, student_course, student_grade)

        cursor.execute(sql, values)
        conn.commit()


    elif action == 2:
        del_student = input("Which student would you like to delete?(id): ")
        
        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (del_student,))
        conn.commit()

    elif action == 3:
        update = input("Which student would y00ou like to update?(id) : ", (id))
        cursor.execute("SELECT name, email, age, course, grade WHERE id=%s",(update,))
        update = cursor.fetchone()
        if user:
            print("Current name", user[0])
            print("Current E-mail", user[1])
            print("Current age", user[2])
            print("Current course", user[3])
            print("Current grade", user[4])
        new_name = input("New name: ")
        new_email = input("New E-mail: ")
        new_age = input("New age: ")
        new_course = input("New course: ")
        new_grade = input("New grade: ")

        


cursor.close()
conn.close()