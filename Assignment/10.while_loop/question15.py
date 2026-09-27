count=0
num = int(input("Enter number : "))
if num>1:
    i=1
    while i!=num+1:
        if i%2!=0:count+=1
        i+=1
print(count)