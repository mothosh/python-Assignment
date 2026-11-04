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
        self.mark = mark

    def calculateGrade(self):
        if self.mark >= 70 and self.mark <= 100:
            self.grade = "A"
        elif self.mark >= 60:
            self.grade = "B"
        elif self.mark >= 50:
            self.grade = "C"
        elif self.mark >= 40:
            self.grade = "D"
        else:
            self.grade = "F"

    def displayStudentDetails(self):
        print(f"Name: {self.name}")
        print(f"Reg No: {self.reg_no}")
        print(f"Course: {self.course}")
        print(f"Mark: {self.mark}")
        print(f"Grade: {self.grade}")
        
s1 = Student()
s1.setStudentDetails("James Mwangi", "BSCIT-01-001/2026", "BSCIT", 85)
s1.calculateGrade()
s1.displayStudentDetails()
