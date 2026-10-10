n = input("Enter signal (red/yellow/green): ").strip().lower()
match n:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")
