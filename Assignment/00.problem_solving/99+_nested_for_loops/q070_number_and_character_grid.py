n = int(input("Enter size: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{chr(64+i)}{j}",end=" ")
    print()