n = input("Enter string: ").split()
for i in n:
    for j in n:
        if i<j:
            print(i,len(i),j,len(j),end=" ")
            if j.startswith(i[0]):print("Same")
            else:print("Different")