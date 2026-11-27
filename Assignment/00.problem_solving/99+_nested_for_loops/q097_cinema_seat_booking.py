s=input("enter rows: ").split(" / ")
a=0
o=0
pr=0
for i in range(len(s)):
    c=0
    for j in s[i]:
        if j=="B":
            a+=1
            c+=1
        elif j=="O":o+=1
    pr=i if c>pr else pr
print(f"Open={a}, Booked={o}; Row {pr} has most space open")