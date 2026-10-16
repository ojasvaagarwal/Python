r=int(input("enter size: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if j%i==0:print(j,end=" ")
    print()