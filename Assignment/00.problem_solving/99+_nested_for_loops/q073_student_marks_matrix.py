data = input("enter marks for all 4 subjects for each student split by (/): ").split("/")
for i in data:
    t=0
    print("marks:",end=" ")
    for j in map(int,i.split()):
        print(j,end=" ")
        t+=j
    print("total:",t,end=" ")
    print("average",t/4)