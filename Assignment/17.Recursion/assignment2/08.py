def d2b(n):
    if n==0:return "0"
    if n==1:return "1"
    k = "1" if n%2 else "0"
    return d2b(n//2) + k

print(d2b(13))
print(d2b(0))
print(d2b(23))