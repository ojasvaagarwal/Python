data = input("enter P/A for each student split by (/): ").split("/")
count=1
for i in data:
    print(f"student {count}",end=" ")
    count+=1
    p=a=0
    for j in i.split():
        if j.upper()=="P":p+=1
        elif j.upper()=="A":a+=1
    print("Present =",p,end=" ")
    print("Absent =",a,end="; ")