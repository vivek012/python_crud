class Student:
    all_student = []
    def __init__(self, name , roll_number , marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks


    def update_marks(self, new_marks):
        self.marks = new_marks  
    

    def show_student_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    @classmethod
    def find_student_by_roll(cls, roll_number):
        for student in cls.all_student:
            if student.roll_number == roll_number:
                return student
        return None

    @classmethod
    def add_student(cls):
        name = input("Enter student name:")
        roll_number = input("Enter student roll number:")
        marks = float(input("Enter student marks:"))
        student = cls(name, roll_number, marks)
        cls.all_student.append(student)
        print(f"Student {name} added successfully.") 


    @classmethod
    def update_student_marks(cls):
        roll = input("Enter student roll number to update marks:")
        student = cls.find_student_by_roll(roll)
        if student:
            new_marks = float(input("Enter new marks:"))
            student.update_marks(new_marks)
            print(f"Marks for student {student.name} updated successfully.")
        else:
            print("Student not found.")


    @classmethod
    def show_all_student(cls):
        if not cls.all_student:
            print("No students found.")
            return
        print("\nList of all students:")
        for student in cls.all_student:
            student.show_student_details()

def menu():
    while True:
        print("\n +=========================== student mananagement System ========================")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. show All Student")
        print("4. Exit")


        choice = int (input("Enten your option(1-4):"))

        if choice == 1:
            Student.add_student()
        elif choice == 2:
            Student.update_student_marks()
        elif choice == 3:
            Student.show_all_student()
        elif choice == 4:
            print("Thank you for using student management system")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":  
    menu()