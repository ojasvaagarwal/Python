while True:
    n = int(input("Enter valid number: "))
    if 10<=n<=50:
        break
if n%2==0:eo="Even"
else:eo="odd"
print(f"Accepted number {n} is {eo}")