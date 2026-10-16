n=int(input("enter a number: "))
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
    print()