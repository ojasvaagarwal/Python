n = int(input("""1 → Student
2 → Teacher
3 → Administration
Enter role: """))
match n:
    case 1:
        m = int(input("""1 → Profile
2 → Marks
3 → Attendance
4 → Courses
Enter option: """))
        match m:
            case 1: print("Opening Student Profile")
            case 2: print("Opening Student Marks")
            case 3: print("Opening Student Attendance")
            case 4: print("Opening Student Courses")
            case _: print("Invalid Option")
    case 2:
        m = int(input("""1 → Students
2 → Enter Marks
3 → Attendance
4 → Courses
Enter option: """))
        match m:
            case 1: print("Opening Teacher Students")
            case 2: print("Opening Teacher Enter Marks")
            case 3: print("Opening Teacher Attendance")
            case 4: print("Opening Teacher Courses")
            case _: print("Invalid Option")
    case 3:
        m = int(input("""1 → Fees
2 → Admissions
3 → Notices
4 → Departments
Enter option: """))
        match m:
            case 1: print("Opening Administration Fees")
            case 2: print("Opening Administration Admissions")
            case 3: print("Opening Administration Notices")
            case 4: print("Opening Administration Departments")
            case _: print("Invalid Option")
    case _: print("Invalid Role")
