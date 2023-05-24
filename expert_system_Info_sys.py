def add_student(students):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    students.append({"Name": name, "Roll No": roll_no, "Branch": branch})
    print("Student added successfully!")


def search_student(students):
    roll_no = input("Enter roll number to search: ")
    found = False
    for student in students:
        if student["Roll No"] == roll_no:
            print("Student found:")
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Branch:", student["Branch"])
            found = True
            break
    if not found:
        print("Student not found.")


def display_all_students(students):
    if not students:
        print("No students found.")
        return
    print("All students:")
    for student in students:
        print("Name:", student["Name"])
        print("Roll No:", student["Roll No"])
        print("Branch:", student["Branch"])


def exit_program():
    print("Exiting the program. Goodbye!")
    exit()


def main():
    students = []
    while True:
        print("\nINFORMATION MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            search_student(students)
        elif choice == "3":
            display_all_students(students)
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()