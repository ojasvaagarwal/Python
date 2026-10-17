def calculate_stats(a, b, c):
    small=min(a,b,c)
    large=max(a,b,c)
    sum=a+b+c
    return small,large,sum
print(calculate_stats(33,44,55))