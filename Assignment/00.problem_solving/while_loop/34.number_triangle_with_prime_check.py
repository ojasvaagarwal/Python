n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        count = 0
        for k in range(1,j+1):
            if j%k == 0:
                count+=1
        if count == 2:
            print("P",end=" ")
        elif j%2 == 0:
            print("E",end=" ")
        else:
            print("O",end=" ")
    print()