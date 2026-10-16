s=input("Enter a alphabet string: ")
for i in range(len(s)):
    for j in range(len(s)):
        if abs(ord(s[i])-ord(s[j])) == 2:
            print(s[i],s[j])