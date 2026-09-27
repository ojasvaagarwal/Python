count = 0
n = int(input("Enter a number : "))
i=1
while i!=n+1:
    if i%2!=0:count+=i
    i+=1
print(count)