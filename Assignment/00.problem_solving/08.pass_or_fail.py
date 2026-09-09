marks = int(input("Enter marks : "))

if marks<0 and marks>100:
    print("Invalid")
elif marks>=40:
    print("Pass")
else:
    print("Fail")