def count_ch(s,s0):
    s,s0=s.lower(),s0.lower()
    def check(i=0,n=""):
        if i==len(s):return n
        if s[i]!=s0:n+=s[i]
        return check(i+1,n)
    return check()
print(count_ch("Ojasva","o"))
print(count_ch("mississippi","s"))