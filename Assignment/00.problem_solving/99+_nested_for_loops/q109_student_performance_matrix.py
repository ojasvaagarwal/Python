nm = input("enter marks m for n students: ").split("/")
x=[f"Subject{i}","Subject2","Subject3","Total",""]
print("|"+"Student\t"+" \t|".join(x))
maxtotal=0
pt=""
for i in range(len(nm)):
    total=0
    for j in nm[i].split():
        total+=int(j)
    if maxtotal < total:
        maxtotal=total
        m=i
    
print("=========================================================================")
print(f"Student with highest total: {m+1}.")