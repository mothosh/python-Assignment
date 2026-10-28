class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

# Example Usage
acc = BankAccount("BSCIT-01-0054/2026", 5000, "21/10/2026", "John Doe")

print(acc.deposit(2000))  # returns 2000
print(acc.withdraw(1000)) # returns 1000
print(acc.withdraw(10000)) # returns insufficient balance

acc.check_balance()
acc.customer_details()
