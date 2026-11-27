def gcd(n1,n2,i=1,m=1):
    m=i if (n1%i==0 and n2%i==0) else m
    if i==n1 or i==n2:return m
    return gcd(n1,n2,i+1,m)

print(gcd(48,18))
print(gcd(36,18))