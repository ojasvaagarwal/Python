a,b=map(int,input("enter 2 numbers: ").split())
if a>b: a,b=b,a
for i in range(1,a+1):
    if a%i==0 and b%i==0:
        print(i,end=" ")