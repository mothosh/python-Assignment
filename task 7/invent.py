inventory = {
    "Milk": 50,
    "Bread": 30,
    "Sugar": 100,
    "Rice": 75,
    "Cooking Oil": 40
}

print("Quantity of Sugar:", inventory["Sugar"])

inventory["Tea Leaves"] = 60

inventory["Bread"] = 45

del inventory["Rice"]

print("\nFinal Inventory:")
print(inventory)
