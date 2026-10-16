r=int(input("enter size: "))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i==j:print("SAME",end=" ")
        else:print("DIFFERENT",end=" ")
    print()