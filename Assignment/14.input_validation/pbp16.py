n1 = float(input("Enter first number: "))

op = input("Enter operator (+, -, *, /): ")
while op != "+" and op != "-" and op != "*" and op != "/":
    print("Invalid operator")
    op = input("Enter operator (+, -, *, /): ")

while True:
    n2 = float(input("Enter second number: "))
    if op != "/" or n2 != 0:
        break
    print("Cannot divide by zero")

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
else:
    result = n1 / n2
print(f"Result: {result}")
