s = input("enter a string: ").strip()
for i in s:
    for j in s:
        if ord(i)-ord(j)>0:print(f"{i}->{j} decreasing")
        elif ord(i)-ord(j)==0:print(f"{i}->{j} same")
        else:print(f"{i}->{j} increasing")