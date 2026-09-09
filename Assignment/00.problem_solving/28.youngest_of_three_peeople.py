name1,name2,name3 = input("Enter all three names (name1 name2 name3) : ").split()
age1,age2,age3 = map(int,input("Enter three ages (age1 age2 age3) : ").split())

if age1==age2 or age2==age3 or age3==age1:
    print("ages are repeated")
else:
    if age1 < age2 and age1 < age3:
        print(f"{name1} is the youngest {age1}")
    elif age2 < age1 and age2 < age3:
        print(f"{name2} is the youngest {age2}")
    elif age3 < age2 and age3 < age1:
        print(f"{name3} is the youngest {age3}")