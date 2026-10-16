r=int(input("enter rows: "))
for i in range(r):
    for j in range(1,r-i+1):
        print(j,end="")
    print()