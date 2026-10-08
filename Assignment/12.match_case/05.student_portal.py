n = int(input("""1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout
Enter choice:"""))
match n:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("loging out...")
    case _:
        print("Invalid Setting")