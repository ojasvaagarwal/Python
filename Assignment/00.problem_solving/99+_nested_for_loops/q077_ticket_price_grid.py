c = int(input("Enter sizeX: "))
r = int(input("Enter sixeY: "))
for i in range(1,r+1):
    for j in range(1,c+1):
        if j%2==0:print(150,end=" ")
        else:print(100,end=" ")
    print()