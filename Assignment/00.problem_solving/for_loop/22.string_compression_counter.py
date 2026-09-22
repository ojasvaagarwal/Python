s=input("Enter a string : ").strip()
a=""
result = ""
for i in s:
    if i not in a:
        a+=i
for j in a:
    count=0
    for k in s:
        count=int(count)
        if j==k:
            count+=1
    count=str(count)
    result = result + j + count
print(result)