s=input("enter a sentence: ").split()
r=""
for i in range(len(s)):
    if s[i] not in r:
        for j in range(len(s)):
            if i<j and s[i]!=s[j]:
                r=r+s[j]+" "
print(r)