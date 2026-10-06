def supermarket_discount():
    purchase_amount = float(input("Enter Total Purchase Amount: Ksh "))

    # iii - Check if qualifies using comparison operator
    qualifies = purchase_amount >= 10000

    if qualifies:
        discount = 0.15 * purchase_amount
    else:
        discount = 0

    # v - Final amount
    final_amount = purchase_amount - discount

    print(f"\n--- Receipt ---")
    print(f"Purchase Amount: Ksh {purchase_amount:.2f}")
    print(f"Qualifies for Discount (>=10000): {qualifies}")
    print(f"Discount (15%): Ksh {discount:.2f}")
    print(f"Final Amount: Ksh {final_amount:.2f}")

supermarket_discount()
