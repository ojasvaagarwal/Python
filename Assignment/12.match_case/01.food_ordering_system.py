menu = ["Pizza","Burger","Pasta","Sandwich"]
choices = []
i=0
while i!=1:
    print("Today's menu :-")
    for j in range(len(menu)):
        print(f"{j+1} -> {menu[j]}")
    choice = int(input("Choice (0 when done): "))
    match choice:
        case 0:
            i=1
        case x if x in range(1,len(menu)+1):
            choices.append(menu[x-1])
        case _:
            print("Invalid Menu Choice")
print(f"You selected {" ".join(choices)}")