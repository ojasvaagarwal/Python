n = int(input("""1 → Student
2 → Teacher
:"""))
match n:
    case 1:
        m = int(input("""1 → View Courses
2 → View Marks
3 → View Attendance
:"""))
        match m:
            case 1:
                print("opening student Courses")
            case 2:
                print("opening student Marks")
            case 3:
                print("opening student Attendance")
            case _:
                print("Invalid")
    case 2:
        m = int(input("""1 → View Students
2 → Enter Marks
3 → View Attendance
:"""))
        match m:
            case 1:
                print("opening teacher Students")
            case 2:
                print("opening teacher Marks")
            case 3:
                print("opening teacher Attendance")
            case _:
                print("Invalid")
    case _:
        print("invalid")