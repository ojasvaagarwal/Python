is_student = input("are you student (y/n): ") == "y"
has_id = input("Do you have an ID? (y/n): ") == "y"
has_ticket = input("Do you have an ticket? (y/n): ") == "y"

if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not Allowed")    