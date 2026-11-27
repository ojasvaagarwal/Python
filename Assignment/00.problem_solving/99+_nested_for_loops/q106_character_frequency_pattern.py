s=input("enter str: ")
s0={i:0 for i in s}
for i in s:
    s0[i]+=1
for i in s0:
    print(i,"*"*s0[i])