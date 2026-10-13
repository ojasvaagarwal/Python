while True:
    n=int(input("enter a marks: "))
    if 1<=n<=100:
        break
if n >= 75:print("Distinction")
elif n >= 60:print("First Class")
elif n >= 35:print("Pass")
else:print("Fail")