# This is a student information manager
import json

def main():
    
    def load_data():
        try:
            with open("students.json", "r") as file:
                students = json.load(file)
        except FileNotFoundError:
            students = []
        return students
    
    def save_data(students):
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
            

    def add_student():
        students = load_data()
        student = {
            "name" : input("Enter the student's name: ").title(),
            "age" : int(input("Enter the student's age: ")),
            "grade" : input("enter the student's grade: ").upper()
        }
        students.append(student)
        save_data(students)
        print("Student added successfully!")
        
    def view_students_data():
        students = load_data()
        if not students:
            print("No students found.")
        else:
            print("Student List:")
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                
                
    def update_student():
        students = load_data()
        search_name = input("Enter the name of the student to update: ").title()
        found = False
        for student in students:
            if student["name"] == search_name:
                found = True
                try:
                    student["age"] = int(input("Enter the new age: "))
                except ValueError:
                    print("Invalid age. Keeping current value.")
                student["grade"] = input("Enter the new grade: ").upper()
                save_data(students)
                print("Student information updated successfully!")
                break
        if not found:
            print("Student not found.")
        
    def delete_student():
        students =load_data()
        search_name = input("Enter the name of the student to delete: ").title()
        found = False
        for student in students[:]:
            if student["name"] == search_name:
                students.remove(student)
                found = True
                break
        if not found:
            print("Student not found.")
        else:
            save_data(students)
            print("Student deleted successfully!")
    
    while True:
        print("====Student Manager==== \n 1. Add student \n 2. View Students \n 3. Update information \n 4. Delete student \n 5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
            
        elif choice == "2":
            view_students_data()
            
        elif choice == "3":
            update_student()
            
        elif choice == "4":
            delete_student()
            
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            
            
if __name__ == "__main__":
    main()