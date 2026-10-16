r=int(input("enter size: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if (i+j)%2==0:print("E",end=" ")
        else:print("O",end=" ")
    print()