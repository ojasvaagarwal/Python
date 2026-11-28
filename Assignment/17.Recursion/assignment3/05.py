def prod(n):
    return 1 if n==0 else n%10 * prod(n//10)
print(prod(int(input("Enter a number: "))))