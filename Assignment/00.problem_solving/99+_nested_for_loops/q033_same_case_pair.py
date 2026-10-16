s = input("enter a number: ")
for i in s:
    for j in s:
        if (i.islower() and j.islower()) or (i.isupper() and j.isupper()):
            print(i,j)