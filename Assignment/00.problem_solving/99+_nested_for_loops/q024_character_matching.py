s0=input("enter a string: ").strip()
s1=input("enter a string: ").strip()
for i in s0:
    for j in s1:
        if i==j:print(f"{i} {j}")