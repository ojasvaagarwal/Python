s = input("Enter a string to check (first single string) : ").split()[0]
char = []
count = 1
for i in s:
    if i in char:
        count+=1
    else:
        char.append(i)
    if count == 2:
        print(f"in {s}, {i} is duplicate")
    elif count == 3 or count == 4:
        print(f"in {s}, {i} is repeated")
    elif count > 4:
        print(f"in {s}, {i} is highly repeated")