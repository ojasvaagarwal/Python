def fibonacci(n):
    if n<=1:return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(6))  # 8