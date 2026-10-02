n = int(input("Enter size of box : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print("*",end="")
        elif (i+j)%2==0:
            print("E",end="")
        else:
            print("O",end="")
    print()