def employee_status():
    """
    This program records employee information including
    their name, age, salary and whether they are currently
    active in the company. It demonstrates use of Boolean
    and string conversion.
    """
    employee_name = "James Mwangi"
    employee_age = 30
    employee_salary = 45000.50
    is_active = True

    print(f"Employee Name: {employee_name}")
    print(f"Employee Age: {employee_age}")
    print(f"Employee Salary: Ksh {employee_salary:.2f}")
    print(f"Active Status: {is_active}")

    age_text = "Employee age is " + str(employee_age) + " years old."
    print(age_text)

employee_status()
