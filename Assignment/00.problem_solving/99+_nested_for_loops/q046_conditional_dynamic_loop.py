n=int(input("enter size: "))
for i in range(1,n+1):
    for j in range(2,i*2+1,2):
        print(j,end=" ")
    print()