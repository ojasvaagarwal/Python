num1,num2,num3 = map(int,input("Enter three numbers (num1 num2 num3) : ").split())

if num1==num2 or num2==num3 or num3==num1:
    print("Numbers are repeated")
else:
    if num1 > num2 and num1 > num3:
        print(f"{num1} is the largest")
    elif num2 > num1 and num2 > num3:
        print(f"{num2} is the largest")
    elif num3 > num2 and num3 > num1:
        print(f"{num3} is the largest")