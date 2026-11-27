def rev(n,r=0):
    if n==0:return r
    r=r*10+n%10
    return rev(n//10,r)
print(rev(1234))
print(rev(4827))