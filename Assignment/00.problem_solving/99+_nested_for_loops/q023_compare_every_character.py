s=input("enter a string: ").strip()
for i in s:
    for j in s:
        if i==j:print(f"{i}/{j} are same")
        else:print(f"{i}/{j} are different")