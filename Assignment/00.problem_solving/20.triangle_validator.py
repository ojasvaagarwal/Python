a,b,c = map(int,input("Enter sides to check triangle validity (a b c) : ").split())

if (a>0 and b>0 and c>0) and (a+b>c and a+c>b and b+c>a): 
    print("Valid triangle")
else:
    print("Invalid triangle")