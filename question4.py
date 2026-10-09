balance = 50000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print("New Balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please try again.")
    input()