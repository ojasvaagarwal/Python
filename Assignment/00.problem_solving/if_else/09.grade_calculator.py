marks = int(input("Enter marks : "))

if marks<0 and marks>100:
    print("Invalid")
elif marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
elif marks>=40:
    print("E")
else:
    print("Fail")