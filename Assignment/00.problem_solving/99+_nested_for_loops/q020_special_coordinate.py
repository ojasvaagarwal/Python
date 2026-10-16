n=int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        if i==j:print("SPECIAL",end=" ")
        elif i+j==n-1:print("PAIR",end=" ")
        else:print("NORMAL",end=" ")
    print()