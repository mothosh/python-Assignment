def calculate_bill(units, cost_per_unit):
    bill = units * cost_per_unit
    return bill

units = float(input("Enter units consumed: "))
cost = float(input("Enter cost per unit: "))

total_bill = calculate_bill(units, cost)

print(f"Total Electricity Bill: KSh {total_bill}")
