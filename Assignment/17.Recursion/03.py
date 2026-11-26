def count(n):
    if n == 0:
        return

    # count(n + 1)
    count(n - 1)

# here Recursion will stop when n becomes 0 and 2 being a positive number n wont become 0 as the expression in increasing.
