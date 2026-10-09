n = int(input("""1 → Savings
2 → Current
:"""))
match n:
    case 1:
        m = int(input("""1 → Check Balance
2 → Deposit
3 → Withdraw
:"""))
        match m:
            case 1:
                print("opening Savings Balance")
            case 2:
                print("opening Savings Deposit")
            case 3:
                print("opening Savings Withdraw")
            case _:
                print("Invalid")
    case 2:
        m = int(input("""1 → Check Balance
2 → Deposit
3 → Withdraw
:"""))
        match m:
            case 1:
                print("opening Current Balance")
            case 2:
                print("opening Current Deposit")
            case 3:
                print("opening Current Withdraw")
            case _:
                print("Invalid")
    case _:
        print("invalid")