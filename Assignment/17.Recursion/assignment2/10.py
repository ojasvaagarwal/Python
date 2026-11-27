def dr(n):
    def digit_sum(n):
        return 0 if n==0 else n%10 + digit_sum(n//10)
    k=digit_sum(n)
    if k<10:return k
    return dr(k)

print(dr(9875))
print(dr(0))