s = input("enter keys: ").split()
for i in range(len(s)):
    for j in range(len(s)):
        print(s[i],len(s[i]),s[j],len(s[j]),"------",abs(len(s[i])-len(s[j])))