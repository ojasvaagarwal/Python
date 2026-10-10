n = int(input("""1 → Start Exam
2 → View Result
3 → Exit
Enter choice: """))
match n:
    case 1:
        age = int(input("Enter age: "))
        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")
    case 2: print("Opening Result")
    case 3: print("Exit...")
    case _: print("Invalid Choice")
