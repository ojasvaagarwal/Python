r = int(input("Enter sizeY : "))
c = int(input("Enter sizeX : "))
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==r-1 or j==c-1:print("*",end="")
        else:print(" ",end="")
    print()