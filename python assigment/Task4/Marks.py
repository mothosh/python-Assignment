def student_marks():
    # i - Create list
    marks = [78, 85, 90, 66, 72]

    # ii - Display all marks
    print(f"All Marks: {marks}")

    # iii - Total using sum()
    total = sum(marks)
    print(f"Total Marks: {total}")

    # iv - Average
    average = total / len(marks)
    print(f"Average Mark: {average:.2f}")

    # v - Highest using max()
    print(f"Highest Mark: {max(marks)}")

    # vi - Lowest using min()
    print(f"Lowest Mark: {min(marks)}")

    # vii - Modify third subject (index 2)
    marks[2] = 95
    print(f"Updated Marks after changing 3rd subject: {marks}")

student_marks()
