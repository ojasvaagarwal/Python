n = int(input("""1 → Flight
2 → Train
3 → Bus
Enter transport: """))
match n:
    case 1:
        m = int(input("""1 → Economy
2 → Business
Enter class: """))
        match m:
            case 1: print("Flight Economy Selected")
            case 2: print("Flight Business Selected")
            case _: print("Invalid Class")
    case 2:
        m = int(input("""1 → Sleeper
2 → AC
Enter class: """))
        match m:
            case 1: print("Train Sleeper Selected")
            case 2: print("Train AC Selected")
            case _: print("Invalid Class")
    case 3:
        m = int(input("""1 → Ordinary
2 → Volvo
Enter class: """))
        match m:
            case 1: print("Bus Ordinary Selected")
            case 2: print("Bus Volvo Selected")
            case _: print("Invalid Class")
    case _: print("Invalid Transport")
