def izprime(n):
    c=0
    for i in range(1,n):
        if n%i==0:c+=1
    return c==1
n = int(input("enter num: "))
for i in range(n):
    for j in range(i,n):
        if izprime(i) and izprime(j) and izprime(i+j):print(i,"+",j,"=",i+j)