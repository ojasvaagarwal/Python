r=int(input("enter rows: "))
c=int(input("enter column: "))
for i in range(1,r+1):
    for j in range(2,c+1,2):
        print(j,end=" ")
    print()