
balance = 75000

print("--- ATM MENU ---")
print("1. Deposit\n2. Withdraw\n3. Transfer\n4. Balance Enquiry\n5. Exit")
choice = int(input("Choose an option (1-5): "))

match choice:
    case 1:
        amount = float(input("Enter deposit amount: ₦"))
        if amount > 0:
            balance += amount
            print(f"Deposit Successful! Current Balance: ₦{balance:,.2f}")
        else:
            print("Transaction Unsuccessful: Deposit amount must be greater than zero.")
    case 2:
        amount = float(input("Enter withdrawal amount: ₦"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"Withdrawal Successful! Current Balance: ₦{balance:,.2f}")
        elif amount <= 0:
            print("Transaction Unsuccessful: Invalid amount.")
        else:
            print("Transaction Unsuccessful: Insufficient funds.")
    case 3:
        acct_num = input("Enter recipient's 10-digit account number: ")
        amount = float(input("Enter transfer amount: ₦"))
        if amount <= balance and amount > 0:
            balance -= amount
            print(f"Transfer of ₦{amount:,.2f} to {acct_num} Successful! Remaining Balance: ₦{balance:,.2f}")
        elif amount <= 0:
            print("Transaction Unsuccessful: Invalid transfer amount.")
        else:
            print("Transaction Unsuccessful: Insufficient funds.")
    case 4:
        print(f"Your Available Balance is: ₦{balance:,.2f}")
    case 5:
        print("Thank you for using our ATM. Goodbye!")
    case _:
        print("Invalid Choice selected.")
