f = open("sales.txt", "a")

product = input("Enter product name: ")
quantity = input("Enter quantity sold: ")
amount = input("Enter total sales amount: ")

print(f"Product: {product}, Quantity: {quantity}, Total Amount: {amount}", file=f)

f.close()
