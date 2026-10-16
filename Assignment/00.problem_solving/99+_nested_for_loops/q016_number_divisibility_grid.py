r=int(input("enter size: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i%j==0:print("X",end=" ")
        else:print("-",end=" ")
    print()