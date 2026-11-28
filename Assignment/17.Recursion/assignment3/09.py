def vc_ct(s):
    return 0 if s=="" else vc_ct(s[1:]) + 1 if s[0] in "aeiou" else vc_ct(s[1:]) + 0
print(vc_ct(input("Enter a str: ")))