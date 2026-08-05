class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.get_grade())
        print("------------------------")


class College:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("\nStudent Details")
        print("========================")
        for student in self.students:
            student.display()

college = College()

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)
    roll = input("Roll Number: ")
    name = input("Name: ")
    marks = float(input("Marks: "))

    s = Student(roll, name, marks)
    college.add_student(s)

college.display_students()