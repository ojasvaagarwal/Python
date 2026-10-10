n = int(input("""1 → Personal Banking
2 → Business Banking
Enter banking type: """))
match n:
    case 1:
        m = int(input("""1 → Balance
2 → Transfer
3 → Loan
Enter option: """))
        match m:
            case 1: print("Personal Balance Selected")
            case 2: print("Personal Transfer Selected")
            case 3: print("Personal Loan Selected")
            case _: print("Invalid Option")
    case 2:
        m = int(input("""1 → Balance
2 → Payroll
3 → Business Loan
Enter option: """))
        match m:
            case 1: print("Business Balance Selected")
            case 2: print("Payroll Selected")
            case 3: print("Business Loan Selected")
            case _: print("Invalid Option")
    case _: print("Invalid Banking Type")
