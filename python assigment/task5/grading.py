def grading_system():
    name = input("Enter Student Name: ")
    mark = int(input("Enter Examination Mark (0-100): "))

    # iii & iv - Grading with if...elif...else
    if mark < 0 or mark > 100:
        grade = "Invalid mark"
    elif mark >= 70:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"

    # v - Display
    print(f"\n--- Result ---")
    print(f"Student: {name}")
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")

grading_system()
