n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j%2==0:print(i,j,i*j)