word = input("Enter a word : ")
nword = ""
for i in word:
    if i in "aeiouAEIOU":
        nword+="@"
    elif i in "qwrtypsdfghijklzxcvbnmQWRTYPLKIHGFDSJZXCVBNM":
        nword+=i.lower()
    elif i in "0987654321":
        nword+="#"
    else:
        nword+="!"
print(nword)