r=int(input("enter size: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i==j:print(1,end=" ")
        else:print(0,end=" ")
    print()