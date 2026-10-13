bb=2000
while True:
    damt=int(input("Enter amt to deposit: "))
    if 0<damt:
        bb+=damt
        break
print(bb)