num = int(input("Enter a number : "))

if num<0:
    print("Negetive")
elif num<=10:
    print("0-10")
elif num<=50:
    print("11-50")
elif num<=100:
    print("51-100")
else:
    print("Above 100")