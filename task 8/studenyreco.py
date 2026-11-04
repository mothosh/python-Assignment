f = open("students.txt", "w")

print("Name: Mary Mueni, Reg: BSCIT-01-001/2026, Course: BIT, Mark: 85", file=f)
print("Name: James Mwangi, Reg: BSCIT-01-002/2026, Course: BSCIT, Mark: 72", file=f)
print("Name: Ann Wanjiru, Reg: BSCIT-01-003/2026, Course: BCA, Mark: 64", file=f)

f.close()

print("File students.txt created successfully.")
