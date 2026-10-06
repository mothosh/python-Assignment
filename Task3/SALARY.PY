def employee_salary():
    employee_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    deduction = float(input("Enter Monthly Deduction: "))

    # iii - Calculate housing allowance 10%
    housing_allowance = 0.10 * basic_salary

    # iv - Gross salary
    gross_salary = basic_salary + housing_allowance

    # v - Net salary
    net_salary = gross_salary - deduction

    # vi - Display
    print(f"\n--- Salary Slip for {employee_name} ---")
    print(f"Basic Salary: Ksh {basic_salary:.2f}")
    print(f"Housing Allowance (10%): Ksh {housing_allowance:.2f}")
    print(f"Gross Salary: Ksh {gross_salary:.2f}")
    print(f"Deduction: Ksh {deduction:.2f}")
    print(f"Net Salary: Ksh {net_salary:.2f}")

employee_salary()
