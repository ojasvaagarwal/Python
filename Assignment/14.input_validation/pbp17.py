bb = 10000
while True:
    while True:
        choice = int(input("""1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
Enter choice: """))
        if choice in (1, 2, 3, 4):
            break
        print("Invalid choice")
    if choice == 1:
        print(f"Balance: ₹{bb}")
    elif choice == 2:
        while True:
            damt = int(input("Enter amount to deposit: "))
            if damt > 0:
                bb += damt
                break
            print("Amount must be greater than zero")
    elif choice == 3:
        while True:
            wamt = int(input("Enter amount to withdraw: "))
            if 0 < wamt <= bb:
                bb -= wamt
                break
            print("Invalid withdrawal amount")
    else:
        print("Exiting")
        break