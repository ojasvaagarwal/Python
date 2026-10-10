n = int(input("""1 → Student
2 → Teacher
3 → Parent
Enter user type: """))
match n:
    case 1:
        m = int(input("""1 → Marks
2 → Attendance
3 → Homework
Enter option: """))
        match m:
            case 1: print("Opening Student Marks")
            case 2: print("Opening Student Attendance")
            case 3: print("Opening Student Homework")
            case _: print("Invalid Option")
    case 2:
        m = int(input("""1 → Enter Marks
2 → Attendance
3 → Assign Homework
Enter option: """))
        match m:
            case 1: print("Opening Teacher Enter Marks")
            case 2: print("Opening Teacher Attendance")
            case 3: print("Opening Teacher Assign Homework")
            case _: print("Invalid Option")
    case 3:
        m = int(input("""1 → Child Marks
2 → Child Attendance
3 → Contact Teacher
Enter option: """))
        match m:
            case 1: print("Opening Child Marks")
            case 2: print("Opening Child Attendance")
            case 3: print("Contacting Teacher")
            case _: print("Invalid Option")
    case _: print("Invalid User Type")
