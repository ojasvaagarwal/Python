s = input("Enter a string to check : ")
dub=[]
rep=[]
hrep=[]
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count+=1
        if count == 2 and s[i] not in dub:
            dub.append(s[i])
        elif 2<count<=4 and s[i] not in rep:
            rep.append(s[i])
            if s[i] in rep:
                dub.remove(s[i])
        elif count>4 and (s[i] not in hrep):
            hrep.append(s[i])
            if s[i] in hrep:
                rep.remove(s[i])

print(f"in {s}, {dub} is duplicate")
print(f"in {s}, {rep} is repeated")
print(f"in {s}, {hrep} is highly repeated")