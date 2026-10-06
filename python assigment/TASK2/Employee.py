def employee_info():
    employee_name = input("Enter Employee Name: ")
    employee_id = input("Enter Employee ID: ")
    employee_age = int(input("Enter Employee Age: "))
    basic_salary = float(input("Enter Basic Salary: "))

    annual_salary = basic_salary * 12

    print(f"\n--- Employee Details ---")
    print(f"Employee Name: {employee_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Employee Age: {employee_age}")
    print(f"Basic Salary: Ksh {basic_salary:.2f}")
    print(f"Annual Salary: Ksh {annual_salary:.2f}")

# Call the function
employee_info()
