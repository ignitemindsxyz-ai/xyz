import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "3rd_database"
)

cursor = conn.cursor()

while True:
    print()
    print("===== Notes =====")
    print("1. Add note")
    print("2. View note")
    print("3. Delete note")
    print("4. Update note")
    print("5. Search by cateogry")
    print("6. Exit")

    choice = input("What would you like to do?(Default = 1) : ")

    if choice == "1" or choice == "":
        title = input("Title(Enter to leave empty): ")
        body = input("Body : ").strip()
        category = input("Which category? : ")

        sql = "INSERT INTO note (title, body, category) VALUES (%s, %s, %s)"
        values = (title, body, category)
        cursor.execute(sql, values)
        conn.commit()

    elif choice == "2":
        cursor.execute("SELECT * FROM note")
        for column in cursor.fetchall():
            print("")
            print(f"ID : {column[0]} \nTitle : {column[1]}\nBody : {column[2]}")
            print("")

    elif choice == "3":
        del_note = input("Which note will be deleted?(id) : ")

        sql = "SELECT * FROM note WHERE id=%s"
        cursor.execute(sql, (del_note,))
        conn.commit()

    elif choice == "4":
        update_note = input("Which note will be updated?(ID) : ")
        cursor.execute("SELECT * FROM note WHERE id=%s", (update_note,))

        notes = cursor.fetchone()
        if notes:
            print(notes[1])
            print(notes[2])
            print()
            new_title = input("New title : ")
            new_body = input("New body : ")

            cursor.execute(
                "UPDATE note SET title=%s, body=%s WHERE id=%s",
                (new_title, new_body, update_note)
            )
            conn.commit()

        else:
            print("Invalid ID")

    elif choice == "5":
        cat_search = input("Which category? : ")
        cursor.execute("SELECT id, title, body, category FROM note WHERE category=%s", (cat_search,))
        notes = cursor.fetchall()
        if notes:
            for note in notes:
                print(f"\nNote ID : {note[0]}")
                print(f"Title : {note[1]}")
                print(f"Body : {note[2]}")
                print(f"Category : {note[3]}")

    elif choice == "6":
        print("Good bye!")
        break