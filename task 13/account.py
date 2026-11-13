# TOPIC 13 Task 3: Simple Banking System

class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.account_number = acc_no
        self.customer_name = name
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            self.balance += amount
            print(f"KSh {amount} deposited to {self.account_number}")
        except ValueError:
            print("Invalid amount! Enter a number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                print(f"Failed: Cannot withdraw KSh {amount} from {self.account_number} - Insufficient balance!")
            else:
                self.balance -= amount
                print(f"KSh {amount} withdrawn from {self.account_number}")
        except ValueError:
            print("Invalid amount! Enter a number.")

    def display(self):
        print(f"Account: {self.account_number} | Name: {self.customer_name} | Balance: KSh {self.balance}")

def performTransaction(account, trans_type, amount):
    if trans_type == "deposit":
        account.deposit(amount)
    elif trans_type == "withdraw":
        account.withdraw(amount)

acc1 = BankAccount("ACC001", "Mary Mueni", 20000)
acc2 = BankAccount("ACC002", "James Mwangi", 15000)

performTransaction(acc1, "deposit", 5000)
performTransaction(acc1, "withdraw", 2000)
performTransaction(acc2, "withdraw", 20000)  
performTransaction(acc2, "deposit", "abc")   

print("\n--- Updated Balances ---")
acc1.display()
acc2.display()

f = open("accounts.txt", "w")
f.write(f"{acc1.account_number}, {acc1.customer_name}, Balance: {acc1.balance}\n")
f.write(f"{acc2.account_number}, {acc2.customer_name}, Balance: {acc2.balance}\n")
f.close()
print("\nSaved to accounts.txt")
