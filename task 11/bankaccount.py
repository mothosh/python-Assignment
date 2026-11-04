class Account:
    def __init__(self):
        self.account_number = ""
        self.balance =0
        
    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: KSh {self.balance}")

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0

    def calculateInterest(self):
        interest = self.balance * self.interest_rate / 100
        return interest

    def displaySavingsAccount(self):
        self.displayAccount()
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Interest Earned: KSh {self.calculateInterest()}")

acc = SavingsAccount()
acc.account_number = "SAV12345"
acc.balance = 50000
acc.interest_rate = 5
acc.displaySavingsAccount()
