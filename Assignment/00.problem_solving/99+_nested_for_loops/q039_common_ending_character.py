s = input("enter keys: ").split()
for i in range(len(s)):
    for j in range(len(s)):
        if i<j and s[j].endswith(s[i][-1]):print(s[i],s[j])