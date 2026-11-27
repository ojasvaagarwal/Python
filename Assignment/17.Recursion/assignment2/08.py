def d2b(n):
    if n==0 or n==1:return f"{n}"
    k = "1" if n%2 else "0"
    return d2b(n//2) + k

print(d2b(13))
print(d2b(0))
print(d2b(23))