s=input("Enter a string: ")
r=0
for i in s:
    if r<s.count(i):
        r=s.count(i)
        h=i
print(h)