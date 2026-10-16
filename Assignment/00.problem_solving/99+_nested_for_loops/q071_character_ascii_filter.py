n = input("Enter string: ")
for i in n:
    for j in n:
        if abs(ord(i)-ord(j))>5:print(i,j)