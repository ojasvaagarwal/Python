n = int(input("""1 → Bronze
2 → Silver
3 → Gold
4 → Platinum
Enter membership level:"""))
match n:
    case 1|2:
        print("Basic Membership")
    case 3|4:
        print("Premium Membership")
    case _:
        print("Invalid selection")