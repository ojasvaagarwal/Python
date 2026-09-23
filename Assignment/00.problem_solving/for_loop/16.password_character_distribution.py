se = input("Enter password : ")
u = 0
l = 0
d = 0
s = 0
for i in se:
    if i >= "a" and i <= "z":
        l += 1
    elif i >= "A" and i <= "Z":
        u += 1
    elif i in "0987654321":
        d += 1
    else:
        s += 1

if u > d and u > s and u > l and u!=d and u!=s and u!=l:
    print(f"Uppercase letters dominated password")
elif l > d and l > s and l > u and l!=d and l!=s and l!=u:
    print(f"Lowercase lettters dominated password")
elif s > d and s > u and s > l and s!=d and s!=u and s!=l:
    print(f"Special charaters dominated password")
elif d > s and d > u and d > l and d!=u and d!=s and d!=l:
    print(f"Digits dominated password")
else:
    print("tie among diffent catogries")
