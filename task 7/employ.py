employees = {
    "Alice": 50000,
    "Brian": 65000,
    "Carol": 45000,
    "David": 70000,
    "Eva": 55000
}

print("Employee Salaries:")
for name, salary in employees.items():
    print(f"{name}: KSh {salary}")

employees["Carol"] = 48000

employees["Frank"] = 60000

total = sum(employees.values())
print(f"\nTotal Salary Payable: KSh {total}")
