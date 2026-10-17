r = int(input("Enter sizeX: "))
c = int(input("Enter sixeY: "))
for i in range(1,r+1):
    for j in range(1,c+1):
        print(f"{chr(64+i)}{j}",end=" ")
    print()