s = input("enter keys: ").split()
for i in range(len(s)):
    for j in range(len(s)):
        if i<j and s[j].startswith(s[i][0]):print(s[i],s[j])