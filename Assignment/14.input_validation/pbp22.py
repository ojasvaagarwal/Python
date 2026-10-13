n = int(input("Enter an integer from 1 to 10: "))
while not 1 <= n <= 10:
    print("Invalid number")
    n = int(input("Enter an integer from 1 to 10: "))
print(f"Accepted number: {n}")
