s=input("enter str: ")
for i in range(len(s)):
    for j in range(len(s)-i-1):
        print("",end=" ")
    for j in range(i+1):
        print(s[j],end=" ")
    print()