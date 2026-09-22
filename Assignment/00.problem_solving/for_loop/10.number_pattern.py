n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%3 == 0  and j%5 == 0:
            print("Z",end=" ")
        elif j%5 == 0:
            print("Y",end=" ")
        elif j%3 == 0:
            print("X",end=" ")
        else:
            print(j,end=" ")
    print()