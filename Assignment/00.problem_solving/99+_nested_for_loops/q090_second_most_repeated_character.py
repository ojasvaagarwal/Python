s=input("Enter a string: ")
r=0
for i in s:
    if r<s.count(i):
        r=s.count(i)
        h=i
r0=0
h=""
for i in s:
    if i not in h and r0<=s.count(i)<r:
        if r0<s.count(i):
            h=""
            r0=s.count(i)
        if r0==s.count(i):
            h=h+i+" "
print(h)