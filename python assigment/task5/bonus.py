def employee_bonus():
    name = input("Enter Employee Name: ")
    years = int(input("Enter Years of Service: "))
    rating = int(input("Enter Performance Rating (1-5): "))

    # iii - Check using logical operators (AND)
    qualifies = years >= 3 and rating >= 4

    # iv, v, vi - Display result
    print(f"\n--- Employee Details ---")
    print(f"Name: {name}")
    print(f"Years of Service: {years}")
    print(f"Performance Rating: {rating}")

    if qualifies:
        print("Result: Employee qualifies for a bonus")
    else:
        print("Result: Employee does not qualify for a bonus")

employee_bonus()
