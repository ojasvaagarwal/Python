n = int(input("""1 → Kilometers to Meters
2 → Meters to Kilometers
3 → Kilograms to Grams
4 → Grams to Kilograms
Enter choice: """))
match n:
    case 1:
        value = int(input("Enter value: "))
        print(f"{value * 1000} meters")
    case 2:
        value = int(input("Enter value: "))
        print(f"{value / 1000} kilometers")
    case 3:
        value = int(input("Enter value: "))
        print(f"{value * 1000} grams")
    case 4:
        value = int(input("Enter value: "))
        print(f"{value / 1000} kilograms")
    case _: print("Invalid Choice")
