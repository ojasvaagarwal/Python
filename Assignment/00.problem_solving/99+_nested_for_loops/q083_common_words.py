data = input("enter keys(/): ").split("/")
r=""
s0=data[0].split()
s1=data[1].split()
for i in range(len(s0)):
    for j in range(len(s1)):
        if s0[i]==s1[j]:
            r=r+s1[j]+" "
            break
print(r)