data = input("enter P/A for each student split by (/): ").split("/")
count=0
h=0
for i in data:
    count+=1
    a=0
    for j in i.split():
        if j.upper()=="A":a+=1
    if a>h:
        h=a
        student=count
print("Student",student)