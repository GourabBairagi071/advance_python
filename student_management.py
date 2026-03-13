# 1.Student Grade Management System 
# Program that records, updates, and deletes student grades. 
# Handle exceptions like invalid student ID, empty grade inputs, and type mismatches. 

class StudentGradeSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        try:
            sid = input("Enter Student ID: ")
            if sid in self.students:
                raise ValueError("Student ID already exists")

            grade = float(input("Enter Grade: "))
            self.students[sid] = grade
            print("Student added successfully")

        except ValueError:
            print("Invalid grade input or duplicate ID")

    def update_student(self):
        try:
            sid = input("Enter Student ID to update: ")

            if sid not in self.students:
                raise KeyError("Student ID not found")

            grade = float(input("Enter new grade: "))
            self.students[sid] = grade
            print("Grade updated successfully")

        except KeyError:
            print("Invalid Student ID")
        except ValueError:
            print("Grade must be a number")

    def delete_student(self):
        try:
            sid = input("Enter Student ID to delete: ")

            if sid not in self.students:
                raise KeyError

            del self.students[sid]
            print("Student deleted successfully")

        except KeyError:
            print("Student ID does not exist")

    def display_students(self):
        if not self.students:
            print("No student records found")
        else:
            for sid, grade in self.students.items():
                print(f"ID: {sid}  Grade: {grade}")


system = StudentGradeSystem()

while True:
    print("\n1.Add Student")
    print("2.Update Grade")
    print("3.Delete Student")
    print("4.Display Students")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.update_student()
    elif choice == "3":
        system.delete_student()
    elif choice == "4":
        system.display_students()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
