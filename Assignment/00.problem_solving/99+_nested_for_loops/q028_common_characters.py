s0=input("enter a string: ").strip()
s1=input("enter a string: ").strip()
count = ""
for i in s0:
    if i not in count:
        for j in s1:
            if i==j and i not in count:count=count+i+" "
print(f"common characters are: {count}")