n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i*j)**(1/2))%1==0:
            print(i,j)