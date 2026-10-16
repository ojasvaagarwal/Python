s = input("enter a number: ").lower()
for i in s:
    for j in s:
        if i in "aeiou" and j in "qwrtyplkjhgfdszxcvbnm":
            print(i,j)