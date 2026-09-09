num = int(input("Enter the number : "))

if num > 0:
    print("Positive", end=" ")
elif num < 0:
    print("Negative", end=" ")

if num == 0:
    print("Zero")
elif num%2 == 0:
    print("Even")
else:
    print("Odd")