s = input("enter a string: ").strip()
for i in s:
    for j in s:
        print(i,j,abs(ord(i)-ord(j)))