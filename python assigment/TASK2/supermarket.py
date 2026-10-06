def supermarket_purchase():
    customer_name = input("Enter Customer Name: ")
    product_name = input("Enter Product Name: ")
    quantity = int(input("Enter Quantity Purchased: "))
    price = float(input("Enter Price per item: "))

    # This calculation multiplies quantity by price to get total cost
    total_cost = quantity * price

    print(f"\n--- Purchase Receipt ---")
    print(f"Customer Name: {customer_name}")
    print(f"Product Name: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Price per Item: Ksh {price:.3f}")
    print(f"Total Cost: Ksh {total_cost:.3f}")

supermarket_purchase()
