string = input("enter a string: ").strip()

for ch in string:
    if string.count(ch) >= 2:
        print(ch)
        break
else:
    print("No repeated character")
