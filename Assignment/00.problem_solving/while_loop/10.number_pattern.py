n = int(input("Enter number of rows : "))
for i in range(n):
    for j in range(1,2*i+2):
        if j%3 == 0  and j%5 == 0:
            print("Z",end=" ")
        elif j%5 == 0:
            print("Y",end=" ")
        elif j%3 == 0:
            print("X",end=" ")
        else:
            print(j,end=" ")
    print()