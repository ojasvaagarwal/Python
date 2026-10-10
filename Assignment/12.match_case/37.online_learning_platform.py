n = int(input("""1 → Programming
2 → Mathematics
3 → Communication
Enter subject: """))
match n:
    case 1:
        m = int(input("""1 → Python
2 → Java
3 → C++
Enter course: """))
        match m:
            case 1: print("Python Selected")
            case 2: print("Java Selected")
            case 3: print("C++ Selected")
            case _: print("Invalid Course")
    case 2:
        m = int(input("""1 → Algebra
2 → Calculus
3 → Statistics
Enter course: """))
        match m:
            case 1: print("Algebra Selected")
            case 2: print("Calculus Selected")
            case 3: print("Statistics Selected")
            case _: print("Invalid Course")
    case 3:
        m = int(input("""1 → English
2 → Presentation
3 → Interview Skills
Enter course: """))
        match m:
            case 1: print("English Selected")
            case 2: print("Presentation Selected")
            case 3: print("Interview Skills Selected")
            case _: print("Invalid Course")
    case _: print("Invalid Subject")
