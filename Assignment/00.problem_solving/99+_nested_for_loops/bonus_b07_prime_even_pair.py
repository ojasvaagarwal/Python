def iz_prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0:count+=1
    if count==2:return True
    else:return False

def iz_evv(n):
    if n%2==0:return True
    else:return False

n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if iz_prime(i+j) and iz_evv(i*j):
            print(i,j)