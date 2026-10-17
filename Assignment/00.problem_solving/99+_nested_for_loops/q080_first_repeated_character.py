s = input("enter word: ").strip()
r=""
for i in range(len(s)):
    for j in range(len(s)):
        if i<j and s[i] not in r:
            if s[i]==s[j]:r=r+s[i]+" "
print(r[0])