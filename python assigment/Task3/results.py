def student_results():
    student_name = input("Enter Student Name: ")
    coursework = float(input("Enter Coursework Mark /30: "))
    exam = float(input("Enter Examination Mark /70: "))

    # ii - Total
    total_mark = coursework + exam

    # iii - Check pass mark using comparison operator
    has_passed = total_mark >= 40

    # iv, v - Display
    print(f"\n--- Student Result ---")
    print(f"Student Name: {student_name}")
    print(f"Coursework: {coursework}/30")
    print(f"Examination: {exam}/70")
    print(f"Total Mark: {total_mark}/100")
    print(f"Passed: {has_passed}")

student_results()
