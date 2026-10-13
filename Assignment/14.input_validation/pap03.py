while True:
    n = int(input("Enter valid age: "))
    if 0<n<=120:
        break
    print("Unrealistic age")
print(f"Accepted age: {n}")