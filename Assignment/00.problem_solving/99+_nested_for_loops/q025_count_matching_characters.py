s0=input("enter a string: ").strip()
s1=input("enter a string: ").strip()
count = 0
for i in s0:
    for j in s1:
        if i==j:count+=1
print(count)