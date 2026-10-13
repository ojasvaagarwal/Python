bb=5000
while True:
    wamt=int(input("Enter amt to withdraw: "))
    if 0<wamt<=bb:
        bb-=wamt
        break
print(bb)