def count_digits(n):
    if -10<n<10:return 1
    return 1 + count_digits(n//10)

print(count_digits(5382))  # 4
print(count_digits(6))     # 1
print(count_digits(0))     # 1
print(count_digits(-123))     # 3