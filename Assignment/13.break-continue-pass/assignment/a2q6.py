seq=input("enter numbers: ").split()
for i in seq:
    if int(i)<0:
        break
    print(i)