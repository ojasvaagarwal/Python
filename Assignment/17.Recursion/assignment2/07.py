def count_ch(s,s0):
    s,s0,l=s.lower(),s0.lower(),len(s)
    def check(i=0,n=""):
        return "" if i==l else s[i] + check(i+1,n) if s[i]!=s0 else check(i+1,n)
    return check()
print(count_ch("Ojasva","o"))
print(count_ch("mississippi","s"))