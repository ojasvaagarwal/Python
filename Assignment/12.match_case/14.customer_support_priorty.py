n = int(input("""1 → Low
2 → Medium
3 → High
4 → Critical
Enter priority:"""))
match n:
    case 1|2:
        print("Normal Priority")
    case 3|4:
        print("Urgent Priority")
    case _:
        print("Invalid selection")