s=input("Enter a string : ").split()
a=[]
result = ""
for i in s:
    if i not in a:
        a.append(i)
for j in a:
    count=0
    for k in s:
        count=int(count)
        if j==k:
            count+=1
    if count>1:
        count=str(count)    
        result = result + j +" - "+ count +" times "
print(result)