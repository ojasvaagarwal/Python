s = input("enter strings: ").split(" / ")
mc=0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        c=0
        for k in s[j]:
            if k in s[i]:c+=1
        if c>mc:mc,wp=c,[s[i],s[j]]
print(" and ".join(wp))