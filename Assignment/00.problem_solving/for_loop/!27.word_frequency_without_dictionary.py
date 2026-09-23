s = input("enter a sentence : ").split()
c=""
for i in s:
    count=1
    if i in c:
        count+=1
    else:
        c=c+i+" "
    if count>1:
        print(i,"-",count,"times")