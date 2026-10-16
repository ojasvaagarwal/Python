n = int(input("Enter size : "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()