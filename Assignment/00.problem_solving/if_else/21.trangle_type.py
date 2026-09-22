a,b,c = map(int,input("Enter sides to check triangle validity (a b c) : ").split())

if (a>0 and b>0 and c>0) and (a+b>c and a+c>b and b+c>a): 
    if a==b==c:
        print("Equilateral Triangle")
    elif (a==b or b==c or c==a):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid triangle")