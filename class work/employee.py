class Employee:
    def __init__(self, employee_id, name, basic_salary, overtime_hours):
        self.employee_id = employee_id
        self.name = name
        self.basic_salary = basic_salary
        self.overtime_hours = overtime_hours

    def calculate_gross_salary(self):
        return self.basic_salary + (self.overtime_hours * 500)

    def calculate_tax(self):
        gross = self.calculate_gross_salary()
        return gross * 0.10

    def calculate_net_salary(self):
        gross = self.calculate_gross_salary()
        tax = self.calculate_tax()
        return gross - tax

emp1 = Employee("EMP101", "Alice", 50000, 10)
emp2 = Employee("EMP102", "Brian", 65000, 6)

for emp in [emp1, emp2]:
    gross = emp.calculate_gross_salary()
    tax = emp.calculate_tax()
    net = emp.calculate_net_salary()
    
    print(f"Employee ID: {emp.employee_id}")
    print(f"Name: {emp.name}")
    print(f"Gross Salary: KSh {gross}")
    print(f"Tax (10%): KSh {tax}")
    print(f"Net Salary: KSh {net}")
    print("-" * 30)
