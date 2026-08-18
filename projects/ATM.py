balance = 1800

while True:
    print("Choose an option.")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    a = int(input("Enter the option: "))

    if a == 1:
        print("Balance:", balance)

    elif a == 2:
        deposit_money = int(input("Enter the deposit money: "))
        if deposit_money > 0:
            balance = balance + deposit_money
            print("Balance after the deposit:", balance)
        else:
            print("Invalid deposit amount!")

    elif a == 3:
        withdrawal_money = int(input("Enter the withdrawal money: "))

        if withdrawal_money <= balance and 0:
            balance = balance - withdrawal_money
            print("Balance after the withdrawal:", balance)
        else:
            print("Invalid withdrawal amount!")

    elif a == 4:
        print("Thank you!")
        break

    else:
        print("Error: enter correct option")