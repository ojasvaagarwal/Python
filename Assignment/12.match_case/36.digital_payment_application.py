n = int(input("""1 → UPI
2 → Card
3 → Wallet
Enter payment type: """))
match n:
    case 1:
        m = int(input("""1 → Scan QR
2 → Enter UPI ID
Enter option: """))
        match m:
            case 1: print("Scan QR Selected")
            case 2: print("Enter UPI ID Selected")
            case _: print("Invalid Option")
    case 2:
        m = int(input("""1 → Credit Card
2 → Debit Card
Enter option: """))
        match m:
            case 1: print("Credit Card Selected")
            case 2: print("Debit Card Selected")
            case _: print("Invalid Option")
    case 3:
        m = int(input("""1 → Add Money
2 → Pay Using Wallet
Enter option: """))
        match m:
            case 1: print("Add Money Selected")
            case 2: print("Pay Using Wallet Selected")
            case _: print("Invalid Option")
    case _: print("Invalid Payment Type")
