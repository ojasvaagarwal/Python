def iz_prime(n,i=2):
    if i==n:return True
    if n%i==0:return False
    i+=1
    return iz_prime(n,i)

print(iz_prime(29))
print(iz_prime(21))
print(iz_prime(7))
print(iz_prime(131))