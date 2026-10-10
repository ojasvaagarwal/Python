n = int(input("""1 → Savings
2 → Current
Enter account type: """))
match n:
    case 1: account = "Savings"
    case 2: account = "Current"
    case _: account = ""
if account:
    print(f"{account} Account")
    amount = float(input("Enter amount: "))
    if amount > 0:
        print("Withdrawal Request Accepted")
    else:
        print("Invalid Amount")
else:
    print("Invalid Account Type")
