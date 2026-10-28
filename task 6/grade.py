def calculate_grade(mark):
    if mark >= 70 and mark <= 100:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

mark = float(input("Enter student's mark: "))

grade = calculate_grade(mark)
print(f"The grade is: {grade}")
