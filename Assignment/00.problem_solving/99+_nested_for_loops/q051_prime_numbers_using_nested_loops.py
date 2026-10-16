def iz_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:count+=1
    if count==2:return True
    else:return False

m=int(input("enter a number: "))
for i in range(1,m+1):
    if iz_prime(i):print(i,end=" ")