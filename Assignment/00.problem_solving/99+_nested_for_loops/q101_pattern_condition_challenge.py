n=int(input("enter num:"))
for i in range(n):
    for j in range(n):
        if i==j and i+j==n-1:print("C",end="")
        elif i==j:print("A",end="")
        elif i+j==n-1:print("B",end="")
        else:print(" ",end="")
    print()