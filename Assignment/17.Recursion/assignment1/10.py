def power(base, exponent):
    if exponent==0:return 1
    return base * power(base,exponent-1)

print(power(2, 5))  # 32
print(power(9, 0))  # 1
print(power(3, 1))  # 3