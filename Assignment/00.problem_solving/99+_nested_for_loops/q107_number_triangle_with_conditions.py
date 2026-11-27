n=int(input("enter size: "))
for i in range(n):
    for j in range(i+1):
        if i==j:
            print("X",end="")
        elif (i+j)%2==0:
            print("E",end="")
        else:
            print("O",end="")
    print()