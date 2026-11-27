def count_ch(s,s0):
    s,s0=s.lower(),s0.lower()
    def check(i=0,n=0):
        if i==len(s):return n
        if s[i]==s0:n+=1
        return check(i+1,n)
    return check()
print(count_ch("Ojasva","o"))