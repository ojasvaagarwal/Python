n = int(input("""1 → Celsius to Fahrenheit
2 → Fahrenheit to Celsius
Enter choice: """))
match n:
    case 1:
        temperature = int(input("Enter temperature: "))
        print(f"Temperature = {temperature * 9 / 5 + 32} F")
    case 2:
        temperature = int(input("Enter temperature: "))
        print(f"Temperature = {(temperature - 32) * 5 / 9} C")
    case _: print("Invalid Choice")
