marks=input("enter numbers: ").split()
for i in marks:
    if int(i)<40:
        continue
    print(i)