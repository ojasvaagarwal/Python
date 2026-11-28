def lfd(n):
    return n if n<10 else lfd(n//10)
print(lfd(int(input("Enter a number: "))))