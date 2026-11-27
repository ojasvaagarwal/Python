s=input("enter rows: ").split(" / ")
a=0
o=0
pr=""
for i in s:
    c=0
    for j in i:
        if j=="1":
            a+=1
            c+=1
        elif j=="0":
            o+=1
    pr+=str(c)+" "
print(f"Available={a}, Occupied={o}; row-wise availability {pr}")