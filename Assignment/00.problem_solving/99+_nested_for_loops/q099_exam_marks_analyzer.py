nm = input("enter marks m for n students: ").split("/")
print("Student Totals ",end="")
maxtotal=0
for i in range(len(nm)):
    total=0
    for j in nm[i].split():
        total+=int(j)
    if maxtotal < total:
        maxtotal=total
        m=i
    print(total,end=" ")
print(f"highest total Student {m+1}.")