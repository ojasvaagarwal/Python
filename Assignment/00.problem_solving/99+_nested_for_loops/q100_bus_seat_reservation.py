s=input("enter rows: ").split(" / ")
a=0
o=0
pr=0
for i in s:
    c=0
    for j in i:
        if j=="1":
            a+=1
            c+=1
        elif j=="0":
            o+=1
    if c==0:pr+=1
print(f"Available={a}, Booked={o}; {pr} fully booked row/s")