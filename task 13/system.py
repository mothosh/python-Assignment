# TOPIC 13 Task 1: Student Management System

class Student:
    def __init__(self):
        self.name = ""
        self.reg_no = ""
        self.course = ""
        self.mark = 0
        self.grade = ""

    def setStudentDetails(self, name, reg_no, course, mark):
        self.name = name
        self.reg_no = reg_no
        self.course = course
        try:
            self.mark = int(mark)
        except ValueError:
            print(f"Invalid mark for {name}, setting to 0")
            self.mark = 0

    def calculateGrade(self):
        if self.mark >= 70:
            self.grade = "A"
        elif self.mark >= 60:
            self.grade = "B"
        elif self.mark >= 50:
            self.grade = "C"
        elif self.mark >= 40:
            self.grade = "D"
        else:
            self.grade = "F"

    def display(self):
        print(f"{self.name} | {self.reg_no} | {self.course} | Mark: {self.mark} | Grade: {self.grade}")

def displayStudents(student_list):
    for s in student_list:
        s.display()


students = []

s1 = Student()
s1.setStudentDetails("Mary Mueni", "BSCIT-001/2026", "BSCIT", 85)
s1.calculateGrade()
students.append(s1)

s2 = Student()
s2.setStudentDetails("James Mwangi", "BSCIT-002/2026", "BBIT", 62)
s2.calculateGrade()
students.append(s2)

s3 = Student()
s3.setStudentDetails("Ann Wanjiru", "BSCIT-003/2026", "BCA", 45)
s3.calculateGrade()
students.append(s3)

displayStudents(students)

f = open("students.txt", "w")
for s in students:
    f.write(f"{s.name}, {s.reg_no}, {s.course}, Mark: {s.mark}, Grade: {s.grade}\n")
f.close()
print("Saved to students.txt")
