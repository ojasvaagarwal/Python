n = int(input("enter grid size : "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i*j)%2 == 0:
            print("E",end=" ")
        elif (i*j)%5 ==0:
            print("F",end=" ")
        elif (i*j)%2 !=0:
            print("O",end=" ")
        else:
            print(i*j,end=" ")
    print()