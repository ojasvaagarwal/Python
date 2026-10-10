n = int(input("""1 → Book Ticket
2 → Cancel Ticket
3 → Check PNR
4 → Train Schedule
5 → Exit
Enter choice: """))
match n:
    case 1: print("Booking Ticket")
    case 2: print("Canceling Ticket")
    case 3: print("Checking PNR")
    case 4: print("Opening Train Schedule")
    case 5: print("Exit...")
    case _: print("Invalid Choice")
