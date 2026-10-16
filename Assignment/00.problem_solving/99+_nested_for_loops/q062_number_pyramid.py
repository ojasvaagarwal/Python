n = int(input("enter a size: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i*2):
        print(j,end="")
    print()