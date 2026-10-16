s = input("enter a string: ").strip()
s0=[]
for i in s:
    count=0
    if i not in s0:
        for j in s:
            if i==j:count+=1
        else:
            s0.append(i)
            print(i,"=",count)