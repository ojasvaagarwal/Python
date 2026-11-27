def answer(n):
    if n == 0:
        return 0

    n + answer(n - 1)

print(answer(3))

# Here a Typeerror rise.
