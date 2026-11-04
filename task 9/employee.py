# File Exception Handling

try:
    f = open("employees.txt", "r")
    
    data = f.read()
    print(data)
    f.close()

except FileNotFoundError:
    print("The employee file was not found.")

finally:
    print("File processing completed.")

print("Program continues running...")
