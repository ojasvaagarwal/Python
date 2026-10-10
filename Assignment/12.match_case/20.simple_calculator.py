first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ").strip()
match operator:
    case "+": print(f"Result = {first + second}")
    case "-": print(f"Result = {first - second}")
    case "*": print(f"Result = {first * second}")
    case "/":
        try:print(f"Result = {first / second:g}")
        except ZeroDivisionError:print(f"infinity")
    case _: print("Invalid Operator")
