def sum_d(n):
    if n==0:return 0
    return n//10%10 + sum_d(n//100)
print(sum_d(583246))