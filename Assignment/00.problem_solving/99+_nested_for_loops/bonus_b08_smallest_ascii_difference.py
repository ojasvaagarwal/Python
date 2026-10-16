s = input("Enter string: ")
r = []
l = 9999999999
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if abs(ord(s[i])-ord(s[j]))<l :
                l=abs(ord(s[i])-ord(s[j]))
                r0=""
            if abs(ord(s[i])-ord(s[j]))==l :
                r0=s[i]+" "+s[j]+"-"
    r+=r0.split("-")
print(r)