try:
    
    age_input = input("Enter your age: ")

    age = int(age_input)
    
    print("Age successfully recorded")
    print(f"Your age is: {age}")

except ValueError:
    print("Invalid age entered")

print("Registration process finished.")
