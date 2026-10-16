n = int(input("enter a number: "))
h=0
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j)
        if i*j>h:h=i*j
print(f"greatest product: {h}")