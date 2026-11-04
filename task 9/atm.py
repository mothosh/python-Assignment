try:
    amount = input("Enter withdrawal amount: ")
    
    amount = int(amount)
    
    print(f"Withdrawal amount: KSh {amount}")

except ValueError:
    print("Invalid amount. Please enter a number.")
