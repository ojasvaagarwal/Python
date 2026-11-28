def length(s):
    return 0 if s=="" else length(s[1:]) + 1
print(length(input("Enter a str: ")))