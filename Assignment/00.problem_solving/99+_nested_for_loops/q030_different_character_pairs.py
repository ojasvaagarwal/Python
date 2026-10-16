s = input("enter a string: ").strip()
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:print(s[i],s[j])