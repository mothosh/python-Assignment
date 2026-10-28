
def calculate_bill(units_consumed, cost_per_unit):
    """Calculates and returns the total electricity bill."""
    bill = units_consumed * cost_per_unit
    return bill

# Main Execution for Task 1
print("--- Task 1: Electricity Bill Calculation ---")
try:
    units = float(input("Enter units consumed: "))
    cost = float(input("Enter cost per unit: "))
    
    total_bill = calculate_bill(units, cost)
    print(f"The total electricity bill is: KSh {total_bill:.2f}\n")
except ValueError:
    print("Invalid input. Please enter numeric values.\n")
