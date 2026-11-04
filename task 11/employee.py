class Employee:
    def __init__(self):
        self.name = ""
        self.employee_id = ""

    def displayEmployee(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")

class Lecturer(Employee):
    def __init__(self):
        super().__init__()
        self.teaching_subject =""
        
    def displayLecturer(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Teaching Subject: {self.teaching_subject}")

lec = Lecturer()
lec.name = "Dr. John Kimani"
lec.employee_id = "EMP101"
lec.teaching_subject = "Python Programming"
lec.displayLecturer()
