s = input("enter a string: ").strip()
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j and s[i]==s[j]:print(f"{s[i]}/{s[j]} is same")
        else:print(f"{s[i]}/{s[j]} is different")