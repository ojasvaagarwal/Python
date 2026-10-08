n = int(input("""1 → Check Balance
2 → Withdraw Money
3 → Deposit Money
4 → Change PIN
5 → Exit
:"""))
match n:
    case 1:
        print("Check Balance Selected")
    case 2:
        print("Withdraw Money Selected")
    case 3:
        print("Deposit Money Selected")
    case 4:
        print("Change PIN Selected")
    case 5:
        print("Exit...")
    case _:
        print("Invalid Selection")