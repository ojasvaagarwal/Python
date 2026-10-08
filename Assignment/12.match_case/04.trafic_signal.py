n = int(input("""1 → Green
2 → Yellow
3 -> Red
Enter signal: """))
match n:
    case 1:
        print("Go")
    case 2:
        print("Wait")
    case 3:
        print("Stop")
    case _:
        print("Invalid Signal")