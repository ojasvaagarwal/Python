s = input("Enter a string to check (single string only) : ")
count = 0
for i in s:
    print(f"charater {i}",end=" ")
    count+=1
    print(f"have position {count}",end=" ")
    if count%2 == 0:
        print("and even",end=" ")
    else:
        print("and odd",end=" ")
    if i in "aeiouAEIOU":
        print("and is vowel")
    elif i in "qwrtypsdfghijklzxcvbnmQWRTYPLKIHGFDSJZXCVBNM":
        print("and is consonent")
    elif i >= chr(48) and i <= chr(57):
        print("and is digit")
    else:
        print("and is special character")