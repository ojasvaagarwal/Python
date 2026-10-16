a,b,c=map(int,input("enter 2 numbers and limit: ").split())
for i in range(1,c+1):
    if i%a==0 and i%b==0:
        print(i,end=" ")