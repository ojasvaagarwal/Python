s = input("enter a sentence: ").split()
for i in range(len(s)):
    for j in range(len(s)):
        if i<j and len(s[i])==len(s[j]):print(s[i],s[j])