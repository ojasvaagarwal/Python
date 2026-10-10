n = int(input("""1 → Employee
2 → Manager
Enter role: """))
match n:
    case 1:
        m = int(input("""1 → View Profile
2 → Apply Leave
3 → View Salary
Enter option: """))
        match m:
            case 1: print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))
                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")
            case 3: print("Opening Employee Salary")
            case _: print("Invalid Option")
    case 2:
        m = int(input("""1 → View Team
2 → Approve Leave
3 → View Reports
Enter option: """))
        match m:
            case 1: print("Opening Team")
            case 2: print("Opening Leave Approvals")
            case 3: print("Opening Reports")
            case _: print("Invalid Option")
    case _: print("Invalid Role")
