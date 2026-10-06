def customer_details():
    # i - Create tuple (cannot be modified)
    customer = ("John Doe", "CUST001", "0712345678", "john@gmail.com")

    # ii - Display complete tuple
    print(f"Complete Customer Tuple: {customer}")

    # iii - Access using indexes (0=name, 2=telephone)
    print(f"Customer Name: {customer[0]}")
    print(f"Telephone Number: {customer[2]}")

    # iv - Number of items using len()
    print(f"Number of items in tuple: {len(customer)}")

    # v - Attempt to modify telephone number
    try:
        customer[2] = "0799999999"
    except TypeError as e:
        print(f"Error when trying to modify: {e}")

    # vi - Explanation
    print("\nReason: Tuples are immutable in Python, meaning their elements cannot be changed after creation. This makes them safe for storing data that should not be modified.")

customer_details()
