n=int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:print("B",end="")
        elif i==j:print("D",end="")
        elif i+j==n-1:print("X",end="")
        else:print(".",end="")
    print()