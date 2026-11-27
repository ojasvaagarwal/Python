q=input("Enter quantities: ").split("/")
p=input("Enter prices: ").split()
print("Totals: ")
for i in q:
    i=i.split()
    total=0
    for j in range(len(i)):
        total+=int(i[j])*int(p[j])
    print(total,end=" ")