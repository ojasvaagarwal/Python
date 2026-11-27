def rev(n,r=0):
    if n==0:return r
    return rev(n//10,r*10+n%10)
print(rev(1234))
print(rev(4827))