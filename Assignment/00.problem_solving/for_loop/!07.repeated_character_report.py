s = input("Enter a string to check string : ")
k = s[::-1]
ch = []
count = 1
for j in range(len(s)):
    for i in range(len(s)):
        if s[i] in ch:
            if s[i] == k[j]:
                count+=1
        else
    if count == 2:
        print(f"in {s}, {i} is duplicate")
    elif count == 3 or count == 4:
        print(f"in {s}, {i} is repeated")
    elif count > 4:
        print(f"in {s}, {i} is highly repeated")