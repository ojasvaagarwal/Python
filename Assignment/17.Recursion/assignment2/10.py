def dr(n):
    def digit_sum(n):
        return 0 if n==0 else n%10 + digit_sum(n//10)
    k=digit_sum(n)
    return k if k<10 else dr(k)

print(dr(9875))
print(dr(0))