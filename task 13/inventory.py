# TOPIC 13 Task 2: Supermarket Inventory

class Product:
    def __init__(self):
        self.name = ""
        self.code = ""
        self.price = 0
        self.quantity = 0

    def setProductDetails(self, name, code, price, quantity):
        try:
            self.name = name
            self.code = code
            self.price = float(price)
            self.quantity = int(quantity)
        except ValueError:
            print(f"Invalid price/quantity for {name}")
            self.price = 0
            self.quantity = 0

    def calculateStockValue(self):
        return self.price * self.quantity

    def display(self):
        print(f"{self.name} ({self.code}) - Price: {self.price}, Qty: {self.quantity}, Value: {self.calculateStockValue()}")

products = []

p1 = Product()
p1.setProductDetails("Sugar", "P001", 150, 100)
products.append(p1)

p2 = Product()
p2.setProductDetails("Flour", "P002", 120, 200)
products.append(p2)

p3 = Product()
p3.setProductDetails("Cooking Oil", "P003", 350, 50)
products.append(p3)

total_value = 0
for p in products:
    p.display()
    total_value += p.calculateStockValue()

print(f"Total Stock Value: KSh {total_value}")

f = open("inventory.txt", "w")
for p in products:
    f.write(f"{p.name}, {p.code}, Price: {p.price}, Qty: {p.quantity}, Value: {p.calculateStockValue()}\n")
f.write(f"TOTAL VALUE: {total_value}\n")
f.close()
