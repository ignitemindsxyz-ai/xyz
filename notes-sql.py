import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "3rd_database"
)

cursor = conn.cursor()

while True:
    print("===== Notes =====")
    print("1. Add note")
    print("2. View note")
    print("3. Delete note")
    print("4. Update note")
    print("5. Exit")

    choice = input("What would you like to do?(Default = 1) : ")

    if choice == "1":
        title = input("Title(Enter to leave empty): ")
        body = input().strip()

        sql = "INSERT INTO note (title, body) VALUES (%s, %s)"
        values = (title, body)
        cursor.execute(sql, values)
        conn.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM note")
        for column in cursor.fetchall():
            print(f"ID = {column[0]} \nTitle : {column[1]}")
            print(f"   Body : {column[2]}")

    elif choice == "3":
        del_note = input("Which note will be deleted?(id) : ")

        sql = "SELECT * FROM note WHERE id=%s"
        cursor.execute(sql, (del_note,))
        conn.commit()