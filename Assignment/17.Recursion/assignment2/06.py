def iz_prime(n,i=2):
    return True if i==n else False if n%i==0 else iz_prime(n,i+1)
print(iz_prime(29))
print(iz_prime(21))
print(iz_prime(7))
print(iz_prime(131))