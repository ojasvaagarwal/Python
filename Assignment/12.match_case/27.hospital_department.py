n = int(input("""1 → General Medicine
2 → Cardiology
3 → Orthopedics
4 → Pediatrics
5 → Emergency
Enter department: """))
match n:
    case 1: print("General Medicine Selected")
    case 2: print("Cardiology Selected")
    case 3: print("Orthopedics Selected")
    case 4: print("Pediatrics Selected")
    case 5: print("Emergency Selected")
    case _: print("Invalid Department")
