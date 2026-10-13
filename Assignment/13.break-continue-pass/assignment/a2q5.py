string =  input("enter a string: ").strip()
tc = input("enter target character: ").strip()[:1]

for i in string:
    print(i)
    if i == tc:
        break