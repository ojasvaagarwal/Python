s=input("enter str: ").split()
for i in range(len(s)):
    print(" ".join(s))
    s.pop()