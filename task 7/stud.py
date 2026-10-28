student = {
    "reg_number": "BSCIT-01-0054/2026",
    "name": "John Doe",
    "course": "BSc Information Technology",
    "year_of_study": 2
}

print("Student Name:", student["name"])
print("Course:", student["course"])

student["year_of_study"] = 3

student["email"] = "john.doe@zetech.ac.ke"

print("\nUpdated Student Record:")
print(student)
