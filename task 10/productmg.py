class Product:
    def __init__(self):
        self.product_name = ""
        self.product_code = ""
        self.price = 0
        self.quantity = 0
        self.stock_value = 0

    def setProductDetails(self, name, code, price, quantity):
        self.product_name = name
        self.product_code = code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        self.stock_value = self.price * self.quantity

    def displayProductDetails(self):
        print(f"Product Name: {self.product_name}")
        print(f"Product Code: {self.product_code}")
        print(f"Price: KSh {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Stock Value: KSh {self.stock_value}")

p1 = Product()
p1.setProductDetails("Sugar", "P001", 150, 100)
p1.calculateStockValue()
p1.displayProductDetails()
