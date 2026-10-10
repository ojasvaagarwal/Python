n = int(input("""1 → Regular
2 → Premium
3 → VIP
Enter ticket type: """))
match n:
    case 1: ticket = "Regular Ticket"
    case 2: ticket = "Premium Ticket"
    case 3: ticket = "VIP Ticket"
    case _: ticket = ""
if ticket:
    age = int(input("Enter age: "))
    if age < 5:
        print("Free Entry")
    else:
        print(ticket, "Selected")
else:
    print("Invalid Ticket Type")
