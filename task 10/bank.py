class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"KSh {amount} deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"KSh {amount} withdrawn.")
        else:
            print("Insufficient balance!")

    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: KSh {self.balance}")

my_account = BankAccount()
my_account.account_number = "12345678"
my_account.customer_name = "Mary Mueni"
my_account.balance = 10000

my_account.deposit(5000)
my_account.withdraw(2000)
my_account.displayAccount()
