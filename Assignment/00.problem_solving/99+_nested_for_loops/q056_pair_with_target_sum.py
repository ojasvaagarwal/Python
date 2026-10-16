n = int(input("enter a number: "))
t = int(input("enter a target: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j == t:print(i,j)