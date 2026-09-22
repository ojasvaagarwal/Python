s = input("Enter password : ")
for i in s:
    u = 0
    l = 0
    d = 0
    s = 0
    if i >= "a" and i <= "z":
        l += 1
    elif i >= "A" and i <= "Z":
        u += 1
    elif i in "0987654321":
        d += 1
    else:
        s += 1
count = l+u+d+s
l = l/count*100
u = u/count*100
d = d/count*100
s = s/count*100
