s = input("Enter a string to check (single string only) : ").strip()
v = d = sc = c = 0
for i in range(len(s)):
    print(f"charater {s[i]}",end=" ")
    print(f"have position {i}",end=" ")
    if i%2 == 0:
        print("and even",end=" ")
    else:
        print("and odd",end=" ")
    if s[i] in "aeiouAEIOU":
        print("and is vowel")
        v+=1
    elif s[i] in "qwrtypsdfghijklzxcvbnmQWRTYPLKIHGFDSJZXCVBNM":
        print("and is consonent")
        c+=1
    elif s[i] >= chr(48) and s[i] <= chr(57):
        print("and is digit")
        d+=1
    else:
        print("and is special character")
        sc+=1
print(f"Vowel: {v} ; Cosonent: {c} ; Digit: {d} ; Special Character: {sc}")