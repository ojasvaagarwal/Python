n = int(input("enter pyramid size : "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        if j%2 == 0:
            print("E",end=" ")
        elif j%3 == 0 and j%5 == 0:
            print("F",end=" ")
        elif j%3 == 0:
            print("T",end=" ")
        elif j%2 != 0:
            print("O",end=" ")
        else:
            print(j,end=" ")
    print()