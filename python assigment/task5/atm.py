def atm_withdrawal():
    # i - Initial balance
    balance = 50000

    # ii, iii - Ask and convert amount
    amount = int(input(f"Your balance is Ksh {balance}. Enter Withdrawal Amount: "))

    # iv, v, vi, vii - Check all conditions
    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
    elif amount > balance:
        print("Error: Insufficient balance. You cannot withdraw more than Ksh 50000.")
    elif amount % 500 != 0:
        print("Error: Amount must be a multiple of Ksh 500.")
    else:
        balance -= amount
        print(f"Withdrawal successful! You have withdrawn Ksh {amount}")
        print(f"Remaining Balance: Ksh {balance}")

atm_withdrawal()
