def max_digit(n,m=0):
    m=n%10 if n%10 > m else m
    if n==0:return m
    return max_digit(n//10,m)

print(max_digit(4729))  # 9
print(max_digit(555))   # 5
print(max_digit(0))     # 0