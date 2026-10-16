n = int(input("enter size: "))
for i in range(n):
    for j in range(1,n-i+1):
        print(j,end=" ")
    print()