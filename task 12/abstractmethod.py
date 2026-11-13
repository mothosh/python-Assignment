from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def makePayment(self):
        pass

class MobileMoneyPayment(Payment):
    def makePayment(self):
        print("Payment made using Mobile Money")

class CardPayment(Payment):
    def makePayment(self):
        print("Payment made using Bank Card")

mobile = MobileMoneyPayment()
card = CardPayment()

mobile.makePayment()
card.makePayment()
